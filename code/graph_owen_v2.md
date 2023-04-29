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


    /tmp/ipykernel_288/2671920032.py:1: FutureWarning: adjacency_matrix will return a scipy.sparse array instead of a matrix in Networkx 3.0.
      mat = nx.adjacency_matrix(graph, dtype=np.int32)



```python
positions = {"a": (0, 0), "b": (1, -2), "c": (1, 2), "d": (2, -2), "e":(2,2)}
nx.draw_networkx_nodes(graph,pos=positions, node_size=500)
nx.draw_networkx_labels(graph, pos=positions, font_color="w")
nx.draw_networkx_edges(graph,pos=positions, arrowstyle="->")
```




    [<matplotlib.patches.FancyArrowPatch at 0x7fb30e2e4430>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2e4670>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2e4a90>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2e4ca0>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2e4fd0>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2ef160>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2ef3a0>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2ef5e0>]




    
![png](output_6_1.png)
    



```python
if nx.is_directed_acyclic_graph(graph):
    print("No cycle in the directed graph")
else:
    print("There are cycle(s) in the directed graph")
```

    No cycle in the directed graph



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




    [<matplotlib.patches.FancyArrowPatch at 0x7fb30e2dd2e0>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2dd520>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2dd940>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2c3d60>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2ddd00>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e2dde80>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e268220>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e268430>,
     <matplotlib.patches.FancyArrowPatch at 0x7fb30e268670>]




    
![png](output_11_1.png)
    



```python
if nx.is_directed_acyclic_graph(graph):
    print("No cycle in the directed graph")
else:
    print("There are cycle(s) in the directed graph")
```

    There are cycle(s) in the directed graph



```python

```
