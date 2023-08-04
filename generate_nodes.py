import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_random_graph_with_50_nodes():
    num_nodes = 50
    graph = nx.Graph()

    nodes = [chr(ord('A') + i) for i in range(num_nodes)]
    graph.add_nodes_from(nodes)

    for i in range(num_nodes):
        num_edges = random.randint(1, 5)  
        neighbors = random.sample(nodes[:i] + nodes[i+1:], num_edges)
        graph.add_edges_from([(nodes[i], neighbor) for neighbor in neighbors])

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=200, font_size=8)
    plt.title("Random Graph with 50 nodes")
    plt.show()

    return graph
