# -----------------------------------------------------------------------------------------------------------------------

# Bellman Ford's algorithm:
# # O(EV)
# works with -ve weights 
# -----------------------------------------------------------------------------------------------------------------------


class GenGraph:
    def __init__(self, num_nodes, edges, directed = False, weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append((node2, weight))
                if not self.directed:
                    self.data[node2].append((node1, weight))

            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not self.directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, values in enumerate(self.data):
                result += "{} : {}\n".format(i, values)
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i,nodes)
        return result

    def __str__(self):
        return self.__repr__()



def bellman_ford(graph, edges):

    # Distance Over-estimation step
    dist = [float('inf')] * len(graph.data)
    dist[0] = 0

    # Distance  Relaxation steps

    for i in range(len(graph.data)):
        for u,v,w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w


    for u,v,e in edges:
        if dist[v] > dist[u] + w:
            return False, dist

    return True, dist



 
num_nodes7 = 5
edges7 = [(0, 1, 4), (0, 2, 2), (1, 3, 2), (1, 4, 3), (1, 2, 3), (2, 1, 1), (2, 4, 5), (2, 3, 4), (4, 3, -5)]
num_nodes7, len(edges7)


graph7 = GenGraph(num_nodes7, edges7, directed = True, weighted=True)
print(graph7)

print(bellman_ford(graph7, edges7))