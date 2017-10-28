# Надеюсь я правильно разобрался в наследовании и сделал так как надо!

from math import pi  # Импортируем значение pi


class F(int):  # Создаем класс, кторый будем наследовать
    def S(self, a, b):  # В нем есть функция площади
        return a * b

    def P(self, a, b):  # И периметра
        return 2 * (a + b)


class Circle(F):  # Класс для кружочков
    def area(self, r):
        a = r
        b = r
        return F.S(self, r, r * pi)  # Ссылаемся на предыдущий класс

    def perimeter(self, r):
        a = 0
        b = pi * r
        return F.P(self, a, b)


class Rectangle(F):  # Класс для прямоугольников
    def area(self, a, b):
        return F.S(self, a, b)  # Такая же отсылка к первому классу

    def perimeter(self, a, b):
        return F.P(self, a, b)


k = int(input("What figure do you want me to explore? If it is a circle input 1, if it is a Rectangle input 2! Your choice: " ))
if k == 1:
    r = int(input("Give me a radius and I will return you an area and perimeter of your circle! Radius: "))
    print("The area of your circle: ", Circle().area(r))
    print("The perimetr of your circle: ", Circle().perimeter(r))
elif k == 2:
    a = int(input("Give me a width and length and I will return you an area and perimeter of your Rectangle! Input only length: "))
    b = int(input("And now input the width: "))
    print("The area of your rectangle: ", Rectangle().area(a, b))
    print("The perimeter of your rectangle : ", Rectangle().perimeter(a, b))
else:
    print("I can explore only circles and rectangles! Input 1 or 2! ")
