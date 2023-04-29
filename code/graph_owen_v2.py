"""
    Owen's Code for a directed graph
"""
    
class DiGraph(object):
    """
    A Directed Graph class
    edges is a dict mapping each node to a list of its children
    """
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.nedges = 0
        self.adjacency_matrix=[[]]

    def add_node(self, name):
        if name in self.nodes:
            print(f'Node {node} already in the graph.  Skip.')
        else:
            self.nodes.append(name)
            self.nnodes +=1
            self.edges[name] = []

    def add_nodes(self, nodes):
        for node in nodes:
            if node in self.nodes:
                print(f'Node {node} already in the graph.  Skip.')
            else:
                self.nodes.append(node)
                self.edges[node] = []
            
    def add_edge(self, src, dest):
        if src not in self.nodes:
            self.add_node(src)
        if dest not in self.nodes:
            self.add_node(dest)
        self.edges[src].append(dest)
        self.nedges += 1 

    def build_adjacency_matrix(self):
        nnodes = self.nnodes
        self.adjacency_matrix = [ [0]*nnodes for _ in range(nnodes)]
        for i in range(nnodes):
            for j in range(nnodes):
                if self.nodes[j] in self.edges[self.nodes[i]]:
                    self.adjacency_matrix[i][j] = 1
    
    def get_neighbors(self, node): 
        if node in self.edges.keys():       
            return self.edges[node]
        else:
            return None
    
    def has_node(self, node):
        return node in self.nodes

    def has_edge(self, source, destination):
        return destination in self.edges[source]
    
    def print_nodes(self):
       return 'Nodes: [' + ','.join(self.nodes) + ']\n'
        
    def print_edges(self):
        result = 'Edges: \n'
        for src in self.edges.keys(): 
            for dest in self.edges[src]:
                result = result + "    (" + src + '-->' + dest + ')\n'
        return result
            
    def print_adjacency_matrix(self):
        result = 'Adjacency Matrix: \n    ['
        for i in range(self.nnodes):
            result += '[' + ','.join([str(k) for k in self.adjacency_matrix[i]]) + ']\n    '
        # Replace last return with ']'
        result = result[:-5]  + ']\n'
        return result
                
    def __str__(self):
        result = ''
        result += self.print_nodes()
        result += self.print_edges()
        result += self.print_adjacency_matrix()
        return result
    
    def detect_cycle(self):
        """
        Detect whether the graph has a cycle
        Returns true if graph is cyclic else false
        """
        visited = {node:False for node in self.nodes}
        recursiveStack = {node:False for node in self.nodes}
        
        for node in self.nodes:
            if visited[node] == False:
                if self.detect_cycle_helper(node, visited, recursiveStack):
                    return True
        return False
    
    def detect_cycle_helper(self, v, visited, recursiveStack):
        """ Mark current node as visited and adds to recursion stack"""
        visited[v] = True
        recursiveStack[v] = True

		# Recursive for all neighbours
		# if any neighbour is visited and in
		# recursiveStack then graph is cyclic
        for neighbor in self.get_neighbors(v):
            if visited[neighbor] == False:
                if self.detect_cycle_helper(neighbor, visited, recursiveStack):
                    return True
            elif recursiveStack[neighbor]:
                return True

        # The node needs to be popped from
        # recursion stack before function ends
        recursiveStack[v] = False
        return False

    

# Undirected Graph
class Graph(DiGraph):

    def add_edge(self, edge):
        DiGraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        DiGraph.add_edge(self, rev)                                            

# Test code
if __name__ == '__main__' :    
    # create the graph 
    graph = DiGraph()

    # add the nodes to the graph
    graph.add_nodes(['a','b','c','d','e'])

    # add the edges to the graph
    graph.add_edge('a','b')
    graph.add_edge('a','c')
    graph.add_edge('a','d')
    graph.add_edge('b','c')
    graph.add_edge('b','d')
    graph.add_edge('c','d')
    graph.add_edge('c','e')
    graph.add_edge('d','e')
    
    # Build Adjacency Matrix
    graph.build_adjacency_matrix()
           
    # print neighbors node C
    neighbors = ','.join(graph.get_neighbors('c'))
    print('Neighbor Nodes that Node C can walk to are: ', neighbors)
    
    # print the graph
    print('The nodes and edges in the graph are:')
    print(graph)
    
    # detect cycle
    if (graph.detect_cycle()):
        print("Graph has at least one cycle.")
    else:
        print("Graph has no cycle.")
        
    print("add a new edge (e-->a)")
    graph.add_edge('e','a') 
    graph.build_adjacency_matrix()    
    # print the graph
    print('The nodes and edges in the graph are:')
    print(graph)
    
    # detect cycle
    if (graph.detect_cycle()):
        print("Graph has at least one cycle.")
    else:
        print("Graph has no cycle.")           