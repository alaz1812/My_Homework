import Help # В Этом файле расположен Ваш код
# Эту реализацию объяснил мне один добрый и терпеливый человек, за что ему огромное спасибо!
# В основе лежит создание одной виртуальной центральной ноды, относительно которй мы будем делать дальнейшие действия

class LinkedCircularList(Help.DoublyLinkedBase):

        def __init__(self):
            self._center = Help._Node(None, None, None)
            self._center._next = self._center  #определяем следующий и
            self._center._prev = self._center  #предыдущий
            self._size = 0

        def add_right(self, e):  # Добавление справа от нашей центральной ноды
            self._insert_between(e, self._center, self._center._next)  # Точно так же как у Вас, увеличивать _Size не надо, так как ссылка это предусматривает

        def add_left(self, e): # Добавление слева от нашей центральной ноды
            self._insert_between(e, self._center._prev, self._center)

        def pop_right(self):  # Удаление справа
            if self.is_empty():   # Этот блок будет почти в каждой функции, на случай, если список пустой
                raise Help.Empty("I am sorry, List is empty")
            return self._delete_node(self._center._next)

        def pop_left(self):  # Удаление слева
            if self.is_empty():
                raise Help.Empty("I am sorry, List is empty")
            return self._delete_node(self._center._prev)

        def next(self, node=0):   # Это как бы вызов следующей ноды
            if self.is_empty():  # Такая же привычная уже нам проверка
                raise Help.Empty("I am sorry, List is empty")
            if node == 0: node = self._center  # Вот это очень важный и положительный момент, мы проверяем, не наша ли виртуальная
            if node._next != self._center:  # центральная нода следующая и, если это не она,
                return node._next  # то просто делаем вызов следующей ноды,
            else:  # а если следующая нода центральная, то нам не нужно ее выводить, поэтому
                return node._next._next  # делаем вызов следующей ноды два раза

        def next_element(self, node=0):  # Это мы перходим к содержимому следующей ноды, к элементу, который в ней находится
            if self.is_empty():
                raise Help.Empty("I am sorry, List is empty")
            if node == 0: node = self._center
            return self.next(node)._element

        def get_element(self, node):  # Берем элемент, который лежит в нашей ноде
            if self.is_empty():
                raise Help.Empty("I am sorry, List is empty")
            return node._element

        def view_list(self):  # обзор нашего кругового списка
            if self.is_empty():
                raise Help.Empty("I am sorry, List is empty")
            node = self.next()
            while node != self._center:  # Вводим пока не дойдем то виртуальной центральной ноды
                print(self.get_element(node), end=' ')
                node = node._next  #
            print()

        def view_elements(self, k):  # вывод k элементов нашего круга
            if self.is_empty():
                raise Help.Empty("I am sorry, List is empty")
            node = self.next()
            for i in range(k): # Очень важный момент! Благодаря продуманной функции get_element
                print(self.get_element(node), end=' ')   # он не выводит нашу центральную ноди и движется погругу!
                node = self.next(node)
            print()


f = LinkedCircularList()

f.add_right(1)
f.add_right(2)
f.add_right(3)

f.add_left(1)
f.add_left(2)
f.add_left(3)
f.add_left(4)
f.add_left(5)

f.view_list()

f.pop_left()

f.view_list()

f.view_elements(20)

# Круто! работает!

