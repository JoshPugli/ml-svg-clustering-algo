from xml.etree.ElementTree import ElementTree, Element, tostring
from sklearn.cluster import KMeans
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])


def extract_colors(svg_path):
    tree = ElementTree()
    tree.parse(svg_path)
    colors = []

    # Regular expression to find RGB hex codes
    hex_pattern = r'#[A-Fa-f0-9]{6}'

    for elem in tree.iter():
        style = elem.attrib.get('style')
        if style:
            colors += re.findall(hex_pattern, style)

    colors = list(set(colors))
    colors_rgb = [list(int(hex[i:i+2], 16) for i in (0, 2, 4))
                  for hex in (color.lstrip('#') for color in colors)]

    return colors_rgb, tree


def apply_kmeans(colors, k):
    colors = np.array(colors)
    kmeans = KMeans(n_clusters=k)
    colors_clustered = kmeans.fit_predict(colors)

    clusters = []
    for i in range(k):
        cluster_data = {}
        cluster = np.where(colors_clustered == i)
        cluster_data['colors'] = [rgb_to_hex(
            color) for color in colors[cluster]]
        cluster_data['center'] = rgb_to_hex(
            list([round(x) for x in kmeans.cluster_centers_[i]]))
        clusters.append(cluster_data)

    return clusters


def find_hex_codes(string):
    try:
        hex_code_pattern = r"#(?:[0-9a-fA-F]{3}){1,2}\b"
        matches = list(re.finditer(hex_code_pattern, string))

        hex_codes = [match.group(0) for match in matches][0]
        indices = [(match.start(), match.end()) for match in matches][0]

        return hex_codes, indices

    except IndexError:
        print("not a color element")
        return None


def adjust_colors(svg_tree: ElementTree, clusters):

    print("BEFORE:\n")
    for e in svg_tree.iter():
        if "style" in e.attrib:
            print(e.attrib["style"])
            
    for e in svg_tree.iter():
        if "style" in e.attrib:
            style = e.attrib["style"]

            if find_hex_codes(style):
                color, indeces = find_hex_codes(style)
                for cluster in clusters:
                    if color in cluster['colors']:

                        replacement = cluster['center']
                        style = e.attrib["style"]

                        e.attrib["style"] = f"{style[:indeces[0]]}{replacement}{style[indeces[1]:]}"
                        
    
    print("\n\nAFTER:\n")
    for e in svg_tree.iter():
        if "style" in e.attrib:
            print(e.attrib["style"])
    
    return svg_tree


def save_svg(svg_tree, output_path):
    svg_tree.write(output_path)


def main(input_svg, output_svg, k):
    colors, svg_tree = extract_colors(input_svg)
    clusters = apply_kmeans(colors, k)
    adjusted_svg = adjust_colors(svg_tree, clusters)
    save_svg(adjusted_svg, output_svg)


main('fish.svg', 'output.svg', 5)
