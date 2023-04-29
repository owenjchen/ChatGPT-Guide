# Owen's Code for a directed graph and an undirected graph 
## Version 2 - using Networkx module


```python
%matplotlib inline
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
```


```python
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
```


```python
nodes = [node for node in graph.nodes()]
nodes
```

    ['a', 'b', 'c', 'd', 'e']




```python
edges = [edge for edge in graph.edges()]
edges
```


    [('a', 'b'),
     ('a', 'c'),
     ('a', 'd'),
     ('b', 'c'),
     ('b', 'd'),
     ('c', 'd'),
     ('c', 'e'),
     ('d', 'e')]




```python
mat = nx.adjacency_matrix(graph, dtype=np.int32)
print(mat.todense())
```

    [[0 1 1 1 0]
     [0 0 1 1 0]
     [0 0 0 1 1]
     [0 0 0 0 1]
     [0 0 0 0 0]]




```python
positions = {"a": (0, 0), "b": (1, -2), "c": (1, 2), "d": (2, -2), "e":(2,2)}
nx.draw_networkx_nodes(graph,pos=positions, node_size=500)
nx.draw_networkx_labels(graph, pos=positions, font_color="w")
nx.draw_networkx_edges(graph,pos=positions, arrowstyle="->")
```

    
![png](../img/output_6_1.png)
    


```python
if nx.is_directed_acyclic_graph(graph):
    print("No cycle in the directed graph")
else:
    print("There are cycle(s) in the directed graph")
```

    No cycle in the directed graph



```python
# Detect cycles in the graph
cycles = list(nx.simple_cycles(graph))

# Print the cycles in the graph
if cycles:
    print("Cycles in the graph:")
    for cycle in cycles:
        print(cycle)
else:
    print("No cycles in the graph")

```

    No cycles in the graph



```python
graph.add_edge('e','a')
```


```python
edges = [edge for edge in graph.edges()]
edges
```


    [('a', 'b'),
     ('a', 'c'),
     ('a', 'd'),
     ('b', 'c'),
     ('b', 'd'),
     ('c', 'd'),
     ('c', 'e'),
     ('d', 'e'),
     ('e', 'a')]




```python
mat = nx.adjacency_matrix(graph, dtype=np.int32)
print(mat.todense())
```

    [[0 1 1 1 0]
     [0 0 1 1 0]
     [0 0 0 1 1]
     [0 0 0 0 1]
     [1 0 0 0 0]]


    /tmp/ipykernel_288/2671920032.py:1: FutureWarning: adjacency_matrix will return a scipy.sparse array instead of a matrix in Networkx 3.0.
      mat = nx.adjacency_matrix(graph, dtype=np.int32)



```python
positions = {"a": (0, 0), "b": (1, -2), "c": (1, 2), "d": (2, -2), "e":(2,2)}
nx.draw_networkx_nodes(graph,pos=positions, node_size=500)
nx.draw_networkx_labels(graph, pos=positions, font_color="w")
nx.draw_networkx_edges(graph,pos=positions, arrowstyle="->")
```

    
![png](../img/output_11_1.png)
    


```python
if nx.is_directed_acyclic_graph(graph):
    print("No cycle in the directed graph")
else:
    print("There are cycle(s) in the directed graph")
```

    There are cycle(s) in the directed graph



```python
# Detect cycles in the graph
cycles = list(nx.simple_cycles(graph))

# Print the cycles in the graph
if cycles:
    print("Cycles in the graph:")
    for cycle in cycles:
        print(cycle)
else:
    print("No cycles in the graph")
```

    Cycles in the graph:
    ['c', 'e', 'a']
    ['c', 'e', 'a', 'b']
    ['c', 'd', 'e', 'a']
    ['c', 'd', 'e', 'a', 'b']
    ['d', 'e', 'a']
    ['d', 'e', 'a', 'b']


