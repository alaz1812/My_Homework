# У меня большие проблемы с тем, чтобы сосолаться на функцию из другого модуля!
# Я умею импортировать модуль, но он у меня тогда его начинает запускать полностью!
# А если я ему пишу так: from Task_1 import factorial ()
# он меня не понимает! Поэтому пришлось копировать!


def factorial(x):
    mult = 1
    for i in range (2,x+1):
        mult = mult * i
    return mult

x = int(input("Hello! We are goig to print out the first n rows of Pascal's triangle! Input the x:  "))
def C(n, k):
    t = factorial(n) // (factorial(n-k) * factorial(k))
    return t

for n in range (0, x + 1):
    print("\n", end=" " * (x - n + 1))
    for k in range (0, n + 1):
        print(C(n, k), end=' ')