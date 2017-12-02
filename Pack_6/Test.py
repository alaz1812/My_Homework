  # Если Вам интересно, то первые три часа ушли на этот код! Только собрался писать комментарии, как вдруг увидел,
  # что не правильно понял задание!!! И что этот класс уже написан Вами!!! А от меня требуется другое!
  # очень растроился, прямо очень!!! Зато стал больше понимать!

class Node:

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

class DLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodesNum = 0

    def addasHead (self, data):
        nodeobj = Node(data)
        if self.head is None:
            self.head = nodeobj
            self.tail = nodeobj
        else:
            self.head.prev = nodeobj
            nodeobj.next = self.head
            self.head = nodeobj
        self.nodesNum = self.nodesNum + 1

    def addasTail (self, data):
        nodeobj = Node(data)
        if self.tail is None:
            self.head = nodeobj
            self.tail = nodeobj
        else:
            self.tail.next = nodeobj
            nodeobj.prev = self.head
            self.tail = nodeobj
        self.nodesNum = self.nodesNum + 1

        def printAll(self, reverse = False):
            if self.head is None:
                print("Sorry, List is empty!!!")
                return

            elif reverse is False:
                t = self.head
                while (t):
                    print (t)
                    t = t.next
                return
            else:
                t = self.tail
                while(t):
                    print(t)
                    t = t.prev
                return


        def allNodes(self):
            return  self.nodesNum

        def removeHead(self):
            if self.head is None:
                print("Sorry, I can't remove the head! There is no elements!!!")
                return
            if self.nodesNum == 1:
                self.head = None
                self.tail = None
                self.nodesNum = self.nodesNum - 1
                return
            t = self.head.next
            self.head.next = None
            self.head = t
            self.head.prev = None
            self.nodesNum = self.nodesNum - 1
            del t


        def removeTail(self):
            if self.tail is None:
                print("Sorry, I can't remove the tail! There is no elements!!!")
                return
            if self.nodesNum == 1:
                self.head = None
                self.tail = None
                self.nodesNum = self.nodesNum - 1
                return
            t = self.tail.prev
            self.tail.prev = None
            self.tail = t
            self.tail.next = None
            self.nodesNum = self.nodesNum - 1
            del t

        def addPos(self, pos, data):
            if pos <=1:
                self.addasHead(data)
                return
            if pos > self.nodesNum:
                self.addasTail(data)
                return

            t = self.head
            for i in range(pos -1):
                t = t.next

            nodeobj = Node(data)
            nodeobj.next = t
            nodeobj.prev = t.prev
            t.prev = nodeobj
            nodeobj.prev.next = nodeobj
            self.nodesNum = self.nodesNum + 1
            del t