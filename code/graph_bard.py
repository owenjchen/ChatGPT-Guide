"""
    Bard's Code for a directed graph
"""
class DirectedGraph:
    """
    A Directed Graph class. This class has the following methods:

    __init__(): This method initializes the graph with the given number of vertices.
    
    add_edge(): This method adds an edge between the given vertices.
    
    remove_edge(): This method removes an edge between the given vertices.
    
    is_edge(): This method checks if there is an edge between the given vertices.
    
    get_neighbors(): This method returns the neighbors of the given vertex.
    
    __repr__(): This method returns a string representation of the graph.
        
"""    

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1

    def remove_edge(self, u, v):
        self.adjacency_matrix[u][v] = 0

    def is_edge(self, u, v):
        return self.adjacency_matrix[u][v] == 1

    def get_neighbors(self, u):
        return [v for v, w in enumerate(self.adjacency_matrix[u]) if w == 1]

    def __repr__(self):
        return str(self.adjacency_matrix)

    def has_cycle(self):
        """
        Returns True if the graph has a cycle, False otherwise.
        """
        # Mark all vertices as unvisited.
        visited = [False] * self.num_vertices
        
        # Iterate over all vertices.
        for u in range(self.num_vertices):
            # If the current vertex is unvisited,
            # do a DFS traversal starting from it.
            if not visited[u]:
                if self._dfs_has_cycle(u, visited):
                    return True

        return False


    def _dfs_has_cycle(self, u, visited):
        """
        Recursively checks if the graph has a cycle, starting from the given vertex.

        Args:
            u: The vertex to start the traversal from.
            visited: A list of booleans indicating which vertices have been visited.

        Returns:
            True if the graph has a cycle, False otherwise.
        """
        # Mark the current vertex as visited.
        visited[u] = True

        # Iterate over all neighbors of the current vertex.
        for v in self.get_neighbors(u):
            # If the current vertex is unvisited,
            # do a recursive DFS traversal starting from it.
            if not visited[v]:
                if self._dfs_has_cycle(v, visited):
                    return True

            # If the current vertex is visited,
            # the graph has a cycle.
            elif visited[v] == True:
                return True

        return False
        
    def find_cycles(self):
        """
        Finds all cycles in the graph and prints the path of each cycle.

        This function works by recursively traversing the graph, starting from each vertex. 
        If the function ever encounters a vertex that has already been visited, it knows that 
        it has found a cycle. The function then adds the current vertex to the cycle and 
        continues traversing the graph.

        Returns:
            A list of lists of vertices, where each list represents a cycle.
        """
        # Mark all vertices as unvisited.
        visited = [False] * self.num_vertices

        # Iterate over all vertices.
        for u in range(self.num_vertices):
            # If the current vertex is unvisited,
            # do a DFS traversal starting from it.
            if not visited[u]:
                cycles = self._dfs_find_cycles(u, visited)
                for cycle in cycles:
                    print(cycle)

        return cycles


    def _dfs_find_cycles(self, u, visited):
        """
        Recursively finds all cycles in the graph, starting from the given vertex.

        Args:
            u: The vertex to start the traversal from.
            visited: A list of booleans indicating which vertices have been visited.

        Returns:
            A list of lists of vertices, where each list represents a cycle.
        """
        # Mark the current vertex as visited.
        visited[u] = True

        # Iterate over all neighbors of the current vertex.
        cycles = []
        for v in self.get_neighbors(u):
            # If the current vertex is unvisited,
            # do a recursive DFS traversal starting from it.
            if not visited[v]:
                cycles.extend(self._dfs_find_cycles(v, visited))

            # If the current vertex is visited,
            # add the current vertex to the current cycle.
            elif visited[v] == True:
                cycle = [u]
                while v != u:
                    cycle.append(v)
                    v = visited[v]
                cycles.append(cycle)

        return cycles
        

#   Here is an example of how to use this class:

g = DirectedGraph(5)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Check if there is an edge between two vertices
print(g.is_edge(0, 1))  # True
print(g.is_edge(0, 4))  # False

# Get the neighbors of a vertex
print(g.get_neighbors(0))  # [1, 2]
print(g.get_neighbors(3))  # [4]

# Print the graph
print(g)  

if g.has_cycle():
    print("Cycle detected!")
else:
    print("No Cycle")

#cycles = graph.find_cycles()
