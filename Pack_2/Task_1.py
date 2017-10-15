def recfact (x):
    if x == 0:
        return 1
    else:
        return x * recfact(x - 1)

def factorial(x):
    mult = 1
    for i in range (2,x+1):
        mult = mult * i
    return mult
x = int(input("Inputn the number: "))
print (recfact(x))
print (factorial(x))
