# Hamiltonian cycle
# A graph that contains a path to all the nodes. ALl the nodes are visited only once and there 
# is a path from end to start . (cycle)

# Euler cycle
# A traversal of the graph where all the edges are visited only once and reach back the staer

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

    def hamiltonian_path(self, path, visited, current):
        if len(path) == self.num_nodes:
            return True

        for av in self.data[current]:
            if not visited[av]:
                visited[av] = True
                path.append(av)
                if self.hamiltonian_path(path, visited, av):
                    return True
                visited[av] = False
                path.remove(av)

        return False
                
    def hamiltonian_cycle(self):
        path = []
        visited = [False] * self.num_nodes

        start = 0
        visited[start] = True
        path.append(start)

        self.hamiltonian_path(path, visited, 0)
        return path


num_nodes = 10

edges = [(0,1), (1,2), (2,3), (3,4), (4,0), (0,5), (1,6), (7,4), (2,8), (3,9), (5,8), (5,9), (6,9), (6,7), (7,8)]

graph = Graph(num_nodes, edges)

print(graph.hamiltonian_cycle())