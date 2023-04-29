"""
    Claude+'s Code for a directed graph
"""

class DirectedGraph:
    def __init__(self, n):
        self.n = n
        self.adj_mat = [[0 for i in range(n)] for j in range(n)]
        
    def add_edge(self, v1, v2):
        self.adj_mat[v1][v2] = 1
        
    def remove_edge(self, v1, v2):
        self.adj_mat[v1][v2] = 0
        
    def has_edge(self, v1, v2):
        return self.adj_mat[v1][v2] == 1
    
    def neighbors(self, v):
        neighbors = []
        for i in range(self.n):
            if self.adj_mat[v][i] == 1:
                neighbors.append(i)
        return neighbors
    
    def has_cycle(self):
        visited = set()
        stack = set()
        
        for v in range(self.n):
            if v in visited:
                continue
                
            if self.has_cycle_helper(v, visited, stack):
                return True
            
        return False

    def has_cycle_helper(self, v, visited, stack):
        visited.add(v)
        stack.add(v)
        
        for neighbor in self.neighbors(v):
            if neighbor in stack:
                return True
            if neighbor not in visited:
                if self.has_cycle_helper(neighbor, visited, stack):
                    return True
        
        stack.remove(v)
        return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("Adjacency Matrix:")
g.display()

if g.detect_cycle():
    print("\nCycle detected!")
else:
    print("\nNo cycle detected.")
    
g.add_edge(3, 0)
if g.detect_cycle():
    print("\nCycle detected!")
else:
    print("\nNo cycle detected.")        