# 0_1 Knapsack
# HOW THE HECK
class weights:
    def __init__(self,name,weight,profit):
        self.name = name
        self.weight = weight
        self.profit = profit


knapsack_weight = 5
list_of_items = [weights(1,1,2),weights(2,3,4),weights(3,2,5),weights(4,2,5)]

main_matrix = [[-1 for x in range(knapsack_weight+1)] for y in range(len(list_of_items)+1)]

for x in range(knapsack_weight+1):
    main_matrix[0][x] = 0
    
for y in range(len(list_of_items)+1):
    main_matrix[y][0] = 0

for y in range(1,knapsack_weight+1):
    for x in range(1,len(list_of_items)+1):
        if (list_of_items[x-1].weight <= y ):
            main_matrix[x][y] = max(list_of_items[x-1].profit + main_matrix[x-1][y-list_of_items[x-1].weight],main_matrix[x-1][y])
        else:
             main_matrix[x][y] = main_matrix[x-1][y]
print(main_matrix)
x = knapsack_weight
y = len(list_of_items)
while(x>0 and y>0):
    if (main_matrix[y][x] == main_matrix[y-1][x]):
        y-=1
    else:
        print(f"take {y}")
        x = x - list_of_items[y-1].weight
        y-=1

        
