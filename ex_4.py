word_1 = "STONE"
word_2 = "LONGEST"
m = len(word_1)
n = len(word_2)
main_matrix = [[-1 for _ in range(len(word_1)+1)] for x in range(len(word_2)+1)]
print(main_matrix)

for x in range(m+1):
    main_matrix[0][x] = 0
for y in range(n+1):
    main_matrix[y][0] = 0

for x in range(1,n+1):
    for y in range(1,m+1):
        if word_1[y-1] == word_2[x-1]:
            main_matrix[x][y] = main_matrix[x-1][y-1] + 1
        else:
            if (main_matrix[x-1][y] > main_matrix[x][y-1]):
                main_matrix[x][y] = main_matrix[x-1][y] 
            else:
                main_matrix[x][y] = main_matrix[x][y-1]


print(m,n)

print(main_matrix)

for x in main_matrix:
    print(x)
l=m
p=n
while (l>0 and p>0):
    if main_matrix[p][l] == main_matrix[p-1][l]:
        p-=1
    elif main_matrix[p][l] == main_matrix[p][l-1]:
        l-=1
    else:
        print(f"letter {word_1[l-1]}")
        p-=1
        l-=1
