nV = 4
INF = 999
G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]

# Floyd's Algorithm
for k in range(nV):
    for i in range(nV):
        for j in range(nV):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

# Print the paths and distances
for i in range(nV):
    for j in range(nV):
        if G[i][j] == INF:
            print("There is no path from node ", i, " to node ", j)
        else:
            path = [i]
            dist = G[i][j]
            while path[-1] != j:
                next_node = min(range(nV), key=lambda k: G[path[-1]][k])
                path.append(next_node)
            print("The path from node ", i, " to node ", j, " is ", path, " with distance ", dist)
