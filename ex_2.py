#job scheduling with deadlines
class mamamiya:
    def __init__(self,job,value,deadline):
        self.job = job
        self.deadline = deadline
        self.value = value
# input area
a = mamamiya(1,5,1)
b = mamamiya(2,10,3)
c = mamamiya(3,15,5)
d = mamamiya(4,7,4)
e = mamamiya(5,8,1)
f = mamamiya(6,9,3)
g = mamamiya(7,4,2)
list_main = [a,b,c,d,e,f,g]
# real code
time_line = [0]*max(list_main,key=lambda x:x.deadline).deadline
sorted_list = sorted(list_main, key=lambda x:x.value,reverse=True)
for x in sorted_list:
    if time_line[x.deadline-1] == 0:
        time_line[x.deadline-1] = x.job
    else:
        for z in range(x.deadline-2,-1,-1):
            if time_line[z] == 0:
                time_line[z] = x.job
                break # do not forget this break

print(time_line)