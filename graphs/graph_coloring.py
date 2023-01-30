class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        for u,v in edges:
            self.data[u].append(v)
            self.data[v].append(u)


    def __str__(self):
        result = ""
        for i,v in enumerate(self.data):
            result += f"{i} -> {v}" + "\n"

        return result

    def is_valid(self, c, color, current):

        for node in self.data[current]:
            if color[node] == c:
                return False

        return True


    def graph_coloring(self, color, max_color, current):
        if current == self.num_nodes:
            return True

        for c in range(1, max_color + 1):
            if self.is_valid(c, color, current):
                color[current] =  c
                if self.graph_coloring(color, max_color, current + 1):
                    return True
                color[current] = 0
        return False



    def coloring(self, max_color):
        color = [0] * self.num_nodes

        return self.graph_coloring(color, max_color, 0), color

# Find all different combinations of options
    def all_graph_coloring(self, color, max_color, current):
        if current == self.num_nodes:
            print("color", color)
            return 

        for c in range(1, max_color + 1):
            if self.is_valid(c, color, current):
                color[current] =  c
                self.all_graph_coloring(color, max_color, current + 1)
                color[current] = 0
    
    def all_coloring_options(self, max_color):
        color = [0] * self.num_nodes

        return self.all_graph_coloring(color, max_color, 0), color

    




num_nodes = 10

edges = [(0,1), (1,2), (2,3), (3,4), (4,0), (0,5), (1,6), (7,4), (2,8), (3,9), (5,8), (5,9), (6,9), (6,7), (7,8)]

graph = Graph(num_nodes, edges)
print(graph)

print(graph.coloring(3))

print(graph.all_coloring_options(3))

