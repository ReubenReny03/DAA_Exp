nV = 4
INF = 999
G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
for k in range(nV):
    for i in range(nV):
        for j in range(nV):
            if (G[i][j]<G[i][k]+G[k][j] and G[i][j]<999):
                print(f"from {i+1} to {j+1} direct is best than {k+1}")
            else:
                 print(f"from {i+1} to {j+1} through {k+1} is better")
            G[i][j] = min(G[i][j],G[i][k]+G[k][j])
            
print(G)