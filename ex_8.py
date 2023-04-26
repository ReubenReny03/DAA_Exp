#krushkals
class storer:
    def __init__(self,frome,toe,weighte):
        self.frome = frome
        self.toe = toe
        self.weighte = weighte

a = storer(0, 1, 1)
b = storer(0, 2, 2)

c = storer(1, 0, 1)
d = storer(1, 2, 3)

e = storer(2,3,6)
f = storer(2,0,2)
g = storer(2,1,3)

h = storer(4,3,6)


list_to_in = [a,b,c,d,e,f,g,h]
already_covered = []
new_sorted_list = sorted(list_to_in, key=lambda x: x.weighte)
already_covered.append(new_sorted_list[0].frome)
for x in new_sorted_list:
    if x.toe not in already_covered:
        print(f"from {x.frome} to {x.toe} the distace is {x.weighte}")
        already_covered.append(x.toe)


