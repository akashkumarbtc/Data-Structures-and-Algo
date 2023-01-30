

def app_pair_shortes(num_nodes, edges):
    distance = [[float('inf')] * num_nodes for _ in range (num_nodes)]

    # all diagnoal elements to 0
    for i in range(num_nodes):
        distance[i][i] = 0

    for u,v,w in edges:
        distance[u][v] = w

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j] )

    return distance




num_nodes = 5
edges = [(0, 1, 4), (0, 2, 2), (1, 3, 2), (1, 4, 3), (1, 2, 3), (2, 1, 1), (2, 4, 5), (2, 3, 4), (4, 3, -5)]

print(app_pair_shortes(num_nodes, edges))