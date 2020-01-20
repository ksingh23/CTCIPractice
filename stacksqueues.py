import sys


class SetOfStacks:
    def __init__(self):
        self.stack_list = []
        self.max_size = 3
        self.current_size = 0

    def push(self, x):
        if self.current_size == 2:
            self.current_size = 0
            s = Stack()
            s.push(x)
            self.stack_list.append(s)
        else:
            if not self.stack_list:
                s = Stack()
                self.stack_list.append(s)
            self.stack_list[-1].push(x)
            self.current_size += 1

    def pop(self):
        if self.stack_list[-1]:
            self.stack_list[-1].pop()
            self.current_size -= 1
            if self.current_size == 0:
                del self.stack_list[-1]


class Stack:
    def __init__(self):
        self.top = None
        self.min = sys.maxsize

    def push(self, x):
        if not self.top:
            self.top = StackNode(x)
            self.top.next = None
        else:
            temp = self.top
            self.top = StackNode(x)
            self.top.next = temp
        if x < self.min:
            self.top.nextMin = self.min
            self.min = x

    def pop(self):
        if self.top.val == self.min:
            self.min = self.top.nextMin
        if self.top:
            if not self.top.next:
                self.top = None
            else:
                self.top = self.top.next

    def get_min(self):
        return self.min

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.val)
            temp = temp.next


class StackNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.nextMin = 0


class MyQueue:
    def __init__(self):
        self.s1, self.s2 = Stack(), Stack()
        self.head = 0
        self.tail = 0

    def push(self, x):
        if not self.s1.top:
            self.head = x
        self.s1.push(x)
        self.tail = self.s1.top.val
        temp = self.s1.top
        while temp:
            self.s2.push(temp.val)
            temp = temp.next

    def pop(self):
        self.s2.pop()
        self.head = self.s2.top.val
        temp = self.s2.top
        self.s1.top = None
        while temp:
            self.s1.push(temp.val)
            temp = temp.next


class SortStack:
    def __init__(self):
        self.s1, self.s2 = Stack(), Stack()

    def push(self, x):
        temp = self.s2.top
        while temp and temp.val < x:
            self.s2.pop()
            self.s1.push(temp.val)
            temp = self.s2.top
        self.s2.push(x)
        temp = self.s1.top
        while temp:
            val = self.s1.top.val
            self.s2.push(val)
            self.s1.pop()
            temp = temp.next

    def pop(self):
        self.s2.pop()


class DogQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x, itr):
        if not self.head:
            node = ShelterNode(x)
            node.iter = itr
            self.head = node
            self.tail = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node = ShelterNode(x)
            node.iter = itr
            temp.next = node

    def pop(self):
        self.head = self.head.next


class CatQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x, itr):
        if not self.head:
            node = ShelterNode(x)
            node.iter = itr
            self.head = node
            self.tail = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node = ShelterNode(x)
            node.iter = itr
            temp.next = node

    def pop(self):
        self.head = self.head.next


class ShelterQueue:
    def __init__(self):
        self.c = CatQueue()
        self.d = DogQueue()
        self.itr = 0

    def enqueue(self, x):
        if x[0] == 'Cat':
            self.c.push(x[1], self.itr)
        elif x[0] == 'Dog':
            self.d.push(x[1], self.itr)
        self.itr += 1

    def deque_any(self):
        if self.c.tail.iter > self.d.tail.iter:
            self.d.pop()
        else:
            self.c.pop()

    def deque_cat(self):
        self.c.pop()

    def deque_dog(self):
        self.d.pop()


class ShelterNode:
    def __init__(self, x):
        self.name = x
        self.next = None
        self.iter = 0