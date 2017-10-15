A = raw_input ("Could I ask you for a number? ")
B = int(A)

def divisors(A):
    help = list()
    help.append(B)
    for i in range(B//2, 0, -1):
        if B % i  == 0:
            help.append(i)
    return help
print (divisors(A))
