# Making a stack in python to practice the language

class Node():
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __str__(self):
        if self.next:
            return '{}, {}'.format(self.data, str(self.next))
        return str(self.data)

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def size(self):
        return self.size

    def push(self, element):
        old_top = self.top
        self.top = Node(element, old_top)
        self.size += 1

    def pop(self):
        if self.top == None:
            return None
        old_top = self.top
        self.top = self.top.next
        self.size -= 1
        return old_top.data

    def peak(self):
        if self.top == None:
            return None
        return self.top.element

    def __str__(self):
        return '[{}]'.format(self.top)
