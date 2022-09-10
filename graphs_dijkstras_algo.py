# -----------------------------------------------------------------------------------------------------------------------

# Dijkstra's algorithm:
# # O(m+n**2)
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





def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    # weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = node[-1]
        
        if distance[current] + weight < distance[node[0]]:
            distance[node[0]] = distance[current] + weight
            if parent:
                parent[node[0]] = current


def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

def shortest_path(graph, start, target):
    visited = [False] * len(graph.data)
    parent  = [None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []

    distance[start] = 0
    queue.append(start)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        # get all neighbors and their distances
        update_distances(graph, current, distance, parent)

        # find the next unvisited node with smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node: 
            queue.append(next_node)
        
    return distance[target], parent



num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
num_nodes7, len(edges7)


graph7 = GenGraph(num_nodes7, edges7, directed = True, weighted=True)
print(graph7)

print(shortest_path(graph7, 0, 5))