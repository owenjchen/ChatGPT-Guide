"""
    Bing's Code for a directed graph
"""

class Graph:
    def __init__(self, num_vertices):
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.num_vertices = num_vertices

    def add_edge(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            print("Invalid vertex!")
        else:
            self.adj_matrix[v1][v2] = 1

    def remove_edge(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            print("Invalid vertex!")
        else:
            self.adj_matrix[v1][v2] = 0

    def display(self):
        for row in self.adj_matrix:
            print()
            for val in row:
                print('{:4}'.format(val), end='')

    def detect_cycle(self):
        visited = [False] * self.num_vertices
        stack_flag = [False] * self.num_vertices
        for node in range(self.num_vertices):
            if not visited[node]:
                if self.detect_cycle_util(node, visited, stack_flag):
                    return True
        return False

    def detect_cycle_util(self, node, visited, stack_flag):
        visited[node] = True
        stack_flag[node] = True
        for neighbor in range(self.num_vertices):
            if not visited[neighbor]:
                if self.adj_matrix[node][neighbor] == 1:
                    if self.detect_cycle_util(neighbor, visited, stack_flag):
                        return True
            elif stack_flag[neighbor]:
                return True
        stack_flag[node] = False
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