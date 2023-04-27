def nqueens(k,n,x):
    for i in range(1,n+1):
        if place(k,i,x):
            x[k] = i
            if k == n:
                print(x[1:])
            else:
                nqueens(k+1,n,x)

def place(k,i,x):
    for j in range(1,k):
        if x[j] == i or abs(x[j] - i ) == abs((j-k)):
            return False
    return True

val_mal = [0]*5
nqueens(1,4,val_mal)