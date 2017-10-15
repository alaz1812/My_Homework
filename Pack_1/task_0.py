A = list(raw_input("Hello! Input a list without gaps: "))
n = len(A) - 1
if n == -1:
    A = "I am sorry, but you didn't input anything"
else:
    x = A[n]
    for i in range(n, 0, -1):
        A [i]= A[i-1]
    A[0]=x
print (A)
print ("Thanks for using me! ")