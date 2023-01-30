# -----------------------------------------------------------------------------------------------------------------------

# Dijkstra's algorithm:
# # O(m+n**2)
# Doesnot work if -ve weights are present
# -----------------------------------------------------------------------------------------------------------------------


class Graph:
    def __init__(self,num_nodes, edges,  weighted=False):
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.data = [[] for _ in range(self.num_nodes)]

        for edge in edges:
            n1, n2, w = edge
            self.data[n1].append((n2, w))
            self.data[n2].append((n1, w))

    def __repr__(self):
        result = ""

        for i, v in enumerate(self.data):
            result += f"{i} -> {v}"

        return result

    def __str__(self):
        return self.__repr__()


    def update_distance(self, distance, current, parent):
        neighbours = self.data[current]

        for edge, weight in neighbours:
            if distance[current] + weight < distance[edge]:
                distance[edge] = distance[current] + weight
                parent[edge] = current


    def pick_next_node(self,  visited, distance):
        min_dist = float('inf')
        min_node = None

        for i in range(len(distance)):
            if not visited[i] and  distance[i] < min_dist:
                min_node = i
                min_dist = distance[i]

        return min_node

    
    def shortest_path(self, start, target):
        visited  = [False] * self.num_nodes
        distance = [float('inf')] * self.num_nodes
        parent = [None] * self.num_nodes

        queue = []
        queue.append(start)
        distance[start] = 0
        visited[start] = True
        idx = 0

        while idx < len(queue):
            current = queue[idx]
            visited[current] = True
            idx += 1

            self.update_distance( distance, current, parent)

            next_node = self.pick_next_node(visited, distance)
            if next_node:
                queue.append(next_node)

        return distance[target], parent 


# num_nodes7 = 6
# edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]


# graph7 = Graph(num_nodes7, edges7,weighted=True)
# print(graph7)

# print(graph7.shortest_path( 0, 5))


# -----------------------------------------------------------------------------------------------------------------------

# Bellman Ford's algorithm:
# # O(EV)
# works with -ve weights 
# -----------------------------------------------------------------------------------------------------------------------


def bellman_ford(edges, num_nodes,  start):
    distance = [float('inf')] * num_nodes
    distance[start] = 0

    for i in range(num_nodes):
        for u,v,w in edges:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    for u,v,w in edges:
        if distance[v] > distance[u] + w:
            return False, distance

    return True, distance


num_nodes6 = 5
edges6 = [(0, 1, 4), (0, 2, 2), (1, 3, 2), (1, 4, 3), (1, 2, 3), (2, 1, 1), (2, 4, 5), (2, 3, 4), (4, 3, -5)]


# graph7 = Graph(num_nodes7, edges7, directed = True, weighted=True)
# print(graph7)

print(bellman_ford(edges6, num_nodes6, 0))