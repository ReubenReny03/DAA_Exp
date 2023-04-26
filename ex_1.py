#The Fractional Knapsack Problem
#items
#weight
#benifit
#value
class items:
    def __init__(self,item,weight,benifit):
        self.item = item
        self.weight = weight
        self.benifit = benifit
        self.value = benifit - weight

#num_of_items = int(input("How many items are there: "))
kanpsak_weight = 5 #int(input("Knapsak Weight : "))
list_of_objects = []
a = items(1,2,5)
b = items(2,2,6)
c = items(3,2,2)
d = items(4,2,3)
e = items(5,2,8)
list_of_objects.append(a)
list_of_objects.append(b)
list_of_objects.append(c)
list_of_objects.append(d)
list_of_objects.append(e)

sorted_list = sorted(list_of_objects, key=lambda x: x.value, reverse=True) #imp
remaning_weight = 0
remaning_item = 0
accepted_list = []
for x in sorted_list:
    if(x.weight<kanpsak_weight):
        accepted_list.append(x.item)
        kanpsak_weight -= x.weight
    elif(x.weight == kanpsak_weight):
        accepted_list.append(x.item)
        break
    else:
        remaning_weight = x.weight/kanpsak_weight
        remaning_item = x.item
        break
print(f"you can have items {accepted_list}")
if remaning_weight != 0:
    print(f"you can also add {remaning_weight} of item {remaning_item}")


    

        

