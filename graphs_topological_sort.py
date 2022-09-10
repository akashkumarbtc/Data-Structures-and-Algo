
# -----------------------------------------------------------------------------------------------------------------------

# Topological sort algorithm
# O(max(v,e))
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



# Kahn's algorithm 

def topological_sort(graph):
    indegree = [0]* len(graph.data)
    result = []
    queue = []

    for i, nodes in enumerate(graph.data):
        for n in nodes:
            indegree[n] += 1

    for idx, indeg in enumerate(indegree):
        if indeg == 0: queue.append(idx)

    idx = 0
    while idx < len(queue):

        current = queue[idx]
        idx += 1

        result.append(current)

        for node in graph.data[current]:
            indegree[node] -= 1
            if  indegree[node] == 0: 
                queue.append(node)

    return result


# Modified BFS algorithm

def modified_bfs(result, graph, visited, vtx):
    visited[vtx] = True
    for node in graph.data[vtx]:
        if visited[node] == False:
            modified_bfs(result, graph, visited, node)

    result.insert(0, vtx)



def topological_sort_bfs(graph):
    result = []
    visited = [False] * len(graph.data)

    modified_bfs(result , graph, visited, 0)

    return result


num_nodes5 = 5
edges5 = [(0, 1),(0, 2), (1, 2), (1, 3), (2, 3), (2, 4)]
graph5 = GenGraph(num_nodes5, edges5, directed = True)
print(graph5)
print(topological_sort(graph5))
print(topological_sort_bfs(graph5))
