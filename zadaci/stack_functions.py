class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    #brisanje
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # vraca true ako je stack prazan i false ako nije
    def is_empty(self):
        return len(self.items) == 0

    # pristupanje posljednjem elementu (elementu na vrhu stacka)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # pristupanje pretposljednjem elementu stacka
    def peek_pretposljednji(self):
        if not self.is_empty():
            return self.items[-2]

    # vracanje cijelog stacka
    def get_stack(self):
        return self.items

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

'''
print(s.is_empty())
s.push(1)
s.push(2)
print(s.is_empty())
print(s.peek())
print(s.get_stack())
s.pop()
print(s.get_stack())
'''

