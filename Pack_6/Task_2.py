import random
# Придется скопировать Ваш класс и чуть изменить его
class _Node:
    def __init__(self, _element, _name, _previous, _next): # Помимо того, что было у Вас будем хранить еще имя сайта
        self._element = _element
        self._name = _name
        self._previous = _previous
        self._next = _next


class DoublyLinkedBase:  # Пришлось чуть переделать Ваш класс
    def __init__(self):
        self._head = _Node(0, None, None, None)  # зададим номера элементов до 10 000
        self._tailer = _Node(10000, None, None, None)
        self._head._next = self._tailer
        self._tailer._previous = self._head
        self._size = 0

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, url, predecessor, successor): # Почти без изменений
        newest= _Node(e, url, predecessor, successor)
        predecessor._next = newest
        successor._previous = newest
        self._size = self._size + 1
        return newest


    def _delete_node(self, node):  # Тоже без изменений
        predecessor = node._previous
        successor = node._next
        predecessor._next = successor
        successor._previous = predecessor
        self._size = self._size - 1
        node._previous = node._next = node._element = None

    def _find_node(self,name):  # Вот, это надо добавить! Поиск ноды
        y = self._head  # Вводим дополнительную переменную
        while y !=self._tailer:
            if y._name == name:
                return y
            y = y._next
        return False

class top_top(DoublyLinkedBase):  # Теперь новый класс! Наш топ!
    def from_site(self, url):  # от сайта, как просили
        s = self._find_node(url) # Вспомогательная переменная
        if s == False:
            return self._insert_between(1, url, self._head, self._head._next)  # присваиваем первый номер
        r = s
        count = s._element
        while (r != self._tailer):
            if count + 1 <= r._next._element:
                self._insert_between(count + 1, url, r, r._next)  # С помощью этой функции добавляем. Не забываем увеличивать номер рейтинга
                return self._delete_node(s)  # И потом возвращаем удаленный
            r = r._next
        return self._insert_between(count + 1, url, self._tailer._previous, self._tailer)

    def from_client(self, k):  # И от клиента
        if not self.is_empty():  # На всякий случай проверим на пустоту
            r = self._tailer._previous
            i = 1
            print("Топ", k, "сайтов: ")
            while r != self._head and i <= k:
                print(str(i) + '.', r._name)  # Печатаем наш топ
                i =i + 1
                r = r._previous


f = top_top()
n = int(input("Добрый день! Введите количество запросов!"))
S = ['web1','web2','web3','web4','web5','web6', 'web7']
for i in range(n):
    h=str(random.choice(S))
    print(h)
    f.from_site(h)
k=int(input("Введите топ скольких сайтов Вы хотите увидеть"))
f.from_client(k)
