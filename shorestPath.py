import cv2
import itertools
import networkx as nx
from scipy.sparse.dok import dok_matrix
from scipy.sparse.csgraph import dijkstra,shortest_path
from sklearn.feature_extraction import image
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
def findShortest(image, original_image):
    # Load the image from disk as a numpy ndarray
    #original_img = cv2.imread('d_test/24.tif')
    original_img = original_image
    # Create a flat color image for graph building:
    #img = cv2.imread('d_test/24.tif', 0)
    img = image

    # Defines a translation from 2 coordinates to a single number, y = height x = width
    def to_index(y, x):
        return y * img.shape[1] + x


    # Defines a reversed translation from index to 2 coordinates
    def to_coordinates(index):
        return index / img.shape[1], index % img.shape[1]

    # A sparse adjacency matrix.
    # Two pixels are adjacent in the graph if both are painted.

    adjacency = dok_matrix((img.shape[0] * img.shape[1], img.shape[0] * img.shape[1]),dtype=np.uint8)
    #adjacency = image.img_to_graph(img)
    #adjacency = np.zeros((img.shape[0]*img.shape[1], img.shape[1]*img.shape[0]))
    # The following lines fills the adjacency matrix by
    directions = list(itertools.product([0, 1, -1], [0, 1, -1]))
    height, width, channels = original_img.shape
    #G2 = nx.complete_graph(height * width)

    #We create a graph the size of our image
    G2 = nx.DiGraph()
    for i in range(width*height):
        G2.add_node(i)

    #These loops create the nodes and the edges between them, the rules are: White pixel to white pixel: lowest cost
    #White to black and black to black: significantly higher cost, node to itself: highest cost to prevemt loops.
    for i in range(0, height):
        for j in range(0, width):
            for y_diff, x_diff in directions:
                if i+y_diff < 0 or i+y_diff > height-1 or j+x_diff < 0 or j+x_diff > width-1:
                    continue
                if img[i + y_diff, j + x_diff]:
                    if to_index(i, j) == to_index(i + y_diff, j + x_diff):
                        #adjacency[to_index(i, j), to_index(i + y_diff, j + x_diff)] = 255

                        G2.add_edge(to_index(i, j), to_index(i + y_diff, j + x_diff), weight=255)
                    else:
                        #print("( {0} , {1} )".format(to_index(i, j), to_index(i + y_diff, j + x_diff)))
                        #adjacency[to_index(i, j), to_index(i + y_diff, j + x_diff)] = True
                        G2.add_edge(to_index(i, j), to_index(i + y_diff, j + x_diff), weight=1)
                else:
                    #print("White to Black")
                    #print(to_index(i, j), to_index(i + y_diff, j + x_diff))
                    #adjacency[to_index(i, j), to_index(i + y_diff, j + x_diff)] = 50
                    G2.add_edge(to_index(i, j), to_index(i + y_diff, j + x_diff), weight=10)
                    #print(adjacency[to_index(i, j), to_index(i + y_diff, j + x_diff)])
                """if i == j:
                    #adjacency[to_index(i, j), to_index(i, j)] = 255
                    G2.add_edge(to_index(i, j), to_index(i + y_diff, j + x_diff), weight=255)"""

    # We chose two arbitrary points, which we know are connected
    source = to_index(1, int((width/2)))
    target = to_index(height-1, int((width/2)))

    print(to_index(height-1, int((width/2)*0.25)))
    #m = adjacency.todense()
    #G = nx.from_numpy_matrix(m, create_using=nx.DiGr aph(),parallel_edges=True)
    #G2 = nx.DiGraph(adjacency)
    #G2 = nx.from_scipy_sparse_matrix(adjacency, create_using=nx.MultiDiGraph)
    """for n, nbrsdict in G.adjacency_iter():
        for nbr,eattr in nbrsdict.items():
            if 'weight' in eattr:
                (n, nbr, eattr['weight'])"""
    #print(G2)

    #G2[0][0]['weight']
    path = nx.shortest_path(G2, source, target, weight='weight')
    print(path)

    # Compute the shortest path between the source and all other points in the image
    """M, predecessors = dijkstra(m, directed=False,
                               unweighted=False, return_predecessors=True) # indices = source,
    """
    # Constructs the path between source and target
    pixel_index = int(target)
    pixels_path = []


    #print(predecessors)
    #print(predecessors[pixel_index-1])
    while pixel_index != source:
        try:
            pixels_path.append(pixel_index)
            pixel_index = path[pixel_index]
        except IndexError:
            print(pixel_index)
            break

    for i in path:
        pixels_path.append(i)
    pixels_path.append(target)
    pixels_path[0] = 0
    # The following code is just for debugging and it visualizes the chosen path
    for pixel_index in pixels_path:
        try:
            i, j = to_coordinates(pixel_index)
            i = int(i)
            j = int(j)
            original_img[i, j, 0] = original_img[i, j, 1] = 5
        except IndexError:
            break
    #cv2.imwrite("d_test/Final Test/img_with_path_weighted_directed_11.tif", original_img)
    #plt.imshow(original_img)
    #plt.show()
    return original_img

for i in range(1, 95):
    img = cv2.imread("largest connected scaled/" + str(i) + ".tif", 0)
    original_image = cv2.imread("processed scaled/" + str(i) + ".tif")
    cv2.imwrite("d_test/Final Test/" + str(i) + ".tif", findShortest(img, original_image))