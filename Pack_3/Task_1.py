class Parentheses:  # Задаем класс скобки
    def validator(self, x):  # Создаем функцию
        a = []  # Список, в который будем записывать скобочки
        skobki = {"(": ")", "{": "}", "[": "]"}  # Гвоздь программы! Словарь! Об этом я прочел здесь https://www.ibm.com/developerworks/ru/library/l-python_part_4/
        for i in x:
            if i in skobki:
                a.append(i)  # Добавляем в нашим список только открывающие скобки
            elif len(a) == 0 or skobki[a.pop()] != i:  # Далее каждой открытой скобке ставим в соответствие закрытую и обе удаляем
                return False  # Если соответствие нарушено, то присвиваем False
        return len(a) == 0


f = input("Input parentheses in any order you want and I will say you wether it is right or not! ")
print(Parentheses().validator(f))

