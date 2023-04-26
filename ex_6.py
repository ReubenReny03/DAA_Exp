def nqueens(k, n, x):
    for i in range(1, n + 1):
        if place(k, i, x):
            x[k] = i
            if k == n:
                print(x[1:])
            else:
                nqueens(k + 1, n, x)
def place(k, i, x):
 for j in range(1, k):
  if x[j] == i or abs(x[j]-i) == abs(j-k):
   return False
 return True

n = int(input("Enter the number of queens:"))
x = [0] * (n+1)
print("All the possible solutions for",n,"queens will be:")
nqueens(1, n, x)
