# -----------------------------------------------------------------------------------------------------------------------

# Mininum Spanning tree - Prims Algorithm
#   O(e*log(v))
# -----------------------------------------------------------------------------------------------------------------------

import heapq

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


def prims(graph, start):
    parent = [-1] * len(graph.data)
    key = [float('inf')] * len(graph.data)
    inMST = [False]* len(graph.data)
    result = []
    key[start] = 0

    heap = []

    heapq.heappush(heap, (0, start))

    while len(heap):
        key_v, vtx = heapq.heappop(heap)

        if parent[vtx] != -1  and inMST[vtx] == False:
            result.append((parent[vtx], vtx, key[vtx]))

        inMST[vtx] = True

        for v,w in graph.data[vtx]:
            if inMST[v] == False and key[v] > w:
                parent[v] = vtx
                key[v] = w
                heapq.heappush(heap, (key[v], v))


    return result







num_nodes3 = 7
edges3 = [(0, 1, 2),(0, 3, 7), (0, 5, 2), (1, 2, 1), (1, 3, 4), (1, 4, 3), (1, 5, 5), (2, 4, 4), (2, 5, 4), (3, 4, 1), (3, 6, 5), (4, 6, 7)]
graph3 = GenGraph(num_nodes3, edges3, weighted = True)
print(graph3)

print(prims(graph3, 0))
# print(kruskal(graph3, edges3))