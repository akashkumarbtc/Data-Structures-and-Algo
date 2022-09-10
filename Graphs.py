
class Graph:

    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [ [] for _ in range(num_nodes)]

        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append[n1]

        
    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in self.data])


    def __str__(self):
        return self.__repr__()

# O(m+n)

def bfs(graph, root):

    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)

    discovered[root] = True
    distance[root] = 0
    queue.append(root)
    idx = 0


    while idx < len(queue):
        current = queue[idx]
        idx += 1

        for node in graph.data[current]:
            if not discovered[node]:
                discovered[node] = True
                distance[node] = 1 + distance[current]
                queue.append(node)

    return queue

# O(m+n)
def dfs(graph, root):
    stack = []
    result = []
    discovered = [False] * len(graph.data)

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        discovered[current] = True
        result.append(current)
        for node in graph.data[current]:
            if not discovered[node]:
                stack.append(node)


    return result




# Graph with weights
num_nodes2 = 9
edges2 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]


# directed graph
num_nodes3 = 5
edges3 = [(0, 1), (1, 2), (2, 3), (2, 4)]


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


# graph2 = GenGraph(num_nodes2, edges2, weighted = True)
# print(graph2)


# graph3 = GenGraph(num_nodes3, edges3, directed = True)
# print(graph3)





num_nodes5 = 5
edges5 = [(0, 1),(0, 2), (1, 2), (1, 3), (2, 3), (2, 4)]
graph5 = GenGraph(num_nodes5, edges5, directed = True)
print(graph5)


print(isCyclePresent(graph5, edges5))

