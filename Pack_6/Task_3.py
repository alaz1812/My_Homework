# очень интересное задание!
# во-первых, Очень важно, что список неубывающий!
# Во-вторых, надо реализовать пробегая Positional Linked List, вот, где, оказывается используется!

import Help

f = Help.PositionalList()

def finder(v):
    a = f._header._next # a будет бежать навстручу b с начала
    b = f._trailer._prev # b - с конца
    while a != b:
        if a._element + b._element == v:  # Если нашли, то просо супер
            return a._element, b._element
        elif a._element + b._element < v: # Если меньше,
            a = a._next  # то сдвигаем а, чтобы увеличить его
        else:
            b = b._prev  # а если больше, то сдвигаем b
    return str("There is no pair of two elements with this sum")


a = input('Введите неубывающий список')
for i in range(len(a)):
    f.add_last(int(a[i]))
v = int(input('Введите сумму, которую будем искать'))
print(finder(v))
#  Это просто прелесть!