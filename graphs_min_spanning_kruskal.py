# -----------------------------------------------------------------------------------------------------------------------

# Mininum Spanning tree - Kruskal Algorithm
#   
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





def find(parent, vtx):
    if vtx != parent[vtx]:
        parent, parent[vtx] = find(parent, parent[vtx])
    return parent, parent[vtx]

def union_set(parent, rank, v_x, v_y):
    parent, rootx = find(parent, v_x)
    parent, rooty = find(parent, v_y)

    if rootx == rooty: return

    if rank[rootx] > rank[rooty]: 
        parent[rooty] = rootx
    else: 
        parent[rootx] = rooty
        if rank[rootx] == rank[rooty]:
            rank[rooty] += 1



def kruskal(graph, edges):
    parent = [i for i in range(len(graph.data))]
    rank = [0] * len(graph.data)
    result = []

    edges.sort(key = lambda x:x[2])
    
    for u, v, w in edges:
        parent, root_u = find(parent, u)
        parent, root_v = find(parent, v)

        if root_u != root_v:
            result.append((u,v,w))
            union_set(parent, rank,root_u,  root_v)

    return result



num_nodes3 = 7
edges3 = [(0, 1, 2),(0, 3, 7), (0, 5, 2), (1, 2, 1), (1, 3, 4), (1, 4, 3), (1, 5, 5), (2, 4, 4), (2, 5, 4), (3, 4, 1), (3, 6, 5), (4, 6, 7)]
graph3 = GenGraph(num_nodes3, edges3, weighted = True)
print(graph3)

print(kruskal(graph3, edges3))