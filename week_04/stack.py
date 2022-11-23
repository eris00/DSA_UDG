class Stack:
    def __init__(self):
        self.items = []

    # dodavanje elementa u stack
    def push(self, item):
        self.items.append(item)

    # brisanje elementa sa vrha stack-a
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            False

    # pristupanje elementu sa vrha stack-a
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(4)
# s.push(9)
#
# print(s.get_stack())