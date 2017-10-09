A = [1, 2, 3, 4, 5]
X = A[4]
for i in range(4, 0, -1):
    A [i]= A[i-1]
A[0]=X
print (A)