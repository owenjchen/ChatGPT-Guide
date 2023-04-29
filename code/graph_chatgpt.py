"""
    ChatGPT's Code for a directed graph
"""
class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        
    def add_edge(self, start_vertex, end_vertex, weight=1):
        self.adj_matrix[start_vertex][end_vertex] = weight
        
    def remove_edge(self, start_vertex, end_vertex):
        self.adj_matrix[start_vertex][end_vertex] = 0
        
    def get_neighbors(self, vertex):
        neighbors = []
        for i in range(self.num_vertices):
            if self.adj_matrix[vertex][i] > 0:
                neighbors.append(i)
        return neighbors
        
    def is_edge(self, start_vertex, end_vertex):
        return self.adj_matrix[start_vertex][end_vertex] > 0
    
    def detect_cycles(self):
        visited = [False] * self.num_vertices
        rec_stack = [False] * self.num_vertices
        for i in range(self.num_vertices):
            if not visited[i]:
                if self.detect_cycles_helper(i, visited, rec_stack):
                    return True
        return False
    
    def detect_cycles_helper(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True
        neighbors = self.get_neighbors(vertex)
        for neighbor in neighbors:
            if not visited[neighbor]:
                if self.detect_cycles_helper(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[vertex] = False
        return False

g = DirectedGraph(5)
# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Adjacency Matrix:")
print(g.adj_matrix)

if g.detect_cycles():
    print("\nCycle detected!")
else:
    print("\nNo cycle detected.")