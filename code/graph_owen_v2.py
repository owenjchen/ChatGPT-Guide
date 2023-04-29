 
"""
    Owen's Code for a directed graph and an undirected graph - using Networkx module
"""

import networkx as nx
import matplotlib.pyplot as plt
graph = nx.DiGraph()
# add the edges to the graph
graph.add_edge('a','b')
graph.add_edge('a','c')
graph.add_edge('a','d')
graph.add_edge('b','c')
graph.add_edge('b','d')
graph.add_edge('c','d')
graph.add_edge('c','e')
graph.add_edge('d','e')

nx.draw_planar(
    graph,
    with_labels=True,
    node_size=1000,
    node_color="#ffff8f",
    width=0.8,
    font_size=14,
)
