
### Color Clustering in SVG Images

This Python script performs color clustering on an SVG image using the K-means algorithm. It identifies distinct colors in the SVG file, groups them into clusters, and replaces similar colors in the image with the representative color of each cluster. The processed SVG file is then saved as the output.

### Dependencies
The following Python libraries are required to run the script:
- `xml.etree.ElementTree`: For parsing SVG files.
- `sklearn.cluster.KMeans`: For performing K-means clustering.
- `bs4.BeautifulSoup`: For parsing and processing SVG files.
- `re`: For regular expressions to extract color codes.
- `numpy`: For numerical computations.
- `matplotlib.pyplot`: For plotting the results.
- `copy.deepcopy`: For deep copying elements of the SVG tree.

### Usage
To use the script, call the `main` function and provide the following parameters:
- `input_svg`: The path to the input SVG file.
- `output_svg`: The path where the processed SVG file will be saved.
- `k`: The number of clusters to create for color grouping.

### Code Explanation
1. `rgb_to_hex(rgb)`: A utility function that converts RGB values to hexadecimal color code format.

2. `extract_colors(svg_path)`: Parses the input SVG file and extracts all unique colors in RGB format. It returns the list of RGB colors and the parsed ElementTree object.

3. `apply_kmeans(colors, k)`: Performs K-means clustering on the RGB colors and returns a list of clusters, each containing colors belonging to that cluster and the representative center color.

4. `find_hex_codes(string)`: A utility function that finds and returns the first hexadecimal color code and its indices in a given string. It is used to identify color elements in the SVG tree.

5. `adjust_colors(svg_tree, clusters)`: Modifies the SVG tree to replace colors with their corresponding cluster center colors.

6. `save_svg(svg_tree, output_path)`: Saves the modified SVG tree to the specified output path.

7. `main(input_svg, output_svg, k)`: The main function that orchestrates the entire process. It extracts colors from the input SVG, applies K-means clustering, adjusts colors in the SVG tree, and saves the processed SVG to the output path.

### Example Usage
```python
main('fish.svg', 'output.svg', 5)
