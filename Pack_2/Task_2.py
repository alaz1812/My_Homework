A = int(input ("Could I ask you for a number? "))
k = 0
for i in range(A//2, 0, -1):
    if A % i  == 0:
        k = k + i
if A == k:
    print ("It is a perfect number")
else:
    print ("It is not a perfect number")

