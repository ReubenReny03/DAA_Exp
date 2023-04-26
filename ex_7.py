
class storer:
    def __init__(self,frome,toe,weighte):
        self.frome = frome
        self.toe = toe
        self.weighte = weighte

class rover:
    def __init__(self,maine):
        self.maine = maine
        self.through = None
        self.weighte = 99999
        self.locked = False

a = storer(0,0,0)
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
p = rover(0)
q = rover(1)
r = rover(2)
s = rover(3)
t = rover(4)
u = rover(5)

rover_list = [p,q,r,s,t,u]

blocked_list = []
used = []

for x in list_to_in:
    temp = x.frome
    ziko = False
    if temp not in used:
        for y in list_to_in:
            used.append(x.frome)
            if (x.frome == temp):
                for j in rover_list:
                    if (j.maine == x.toe and j.locked ==False ):
                        ziko == True
                        if (j.weighte > x.weighte):
                            j.weighte = x.weighte
                            j.through = x.frome
    if (ziko == True):
        a = min(rover_list, key=lambda x:x.weighte and x.locked == False)
        a.locked = True

for x in rover_list:
    print(x.maine,x.through,x.weighte)

    


