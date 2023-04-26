class storer:
    def __init__(self,frome,toe,weighte):
        self.frome = frome
        self.toe = toe
        self.weighte = weighte

a = storer(0, 1, 4)
b = storer(0, 2, 4)
c = storer(1, 2, 2)
d = storer(1, 0, 4)
e = storer(2, 0, 4)
f = storer(2, 1, 2)
g = storer(2, 3, 3)
h = storer(2, 5, 2)
i = storer(2, 4, 4)
j = storer(3, 2, 3)
k = storer(3, 4, 3)
l = storer(4, 2, 4)
m = storer(4, 3, 3)
n = storer(5, 2, 2)
o = storer(5, 4, 3)

list_to_in = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
already_covered = []
new_sorted_list = sorted(list_to_in, key=lambda x: x.weighte)
for x in new_sorted_list:
    if x.toe not in already_covered:
        print(f"from {x.frome} to {x.toe} the distace is {x.weighte}")
        already_covered.append(x.toe)


