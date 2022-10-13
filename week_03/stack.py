class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def even_odd(self, s2):
        s1 = Stack()
        while not self.is_empty():
            element = self.pop()
            if element % 2 == 0:
                s1.push(element)
            else:
                s2.push(element)
        return s1, s2

    def in_binary(self, num):
        s = Stack()
        while num > 0:
            reminder = num
            s.push(reminder)
            num = num // 2
        binary_num = " "
        while not s.is_empty():
            binary_num = binary_num+str(s.pop)
        return binary_num
        print(in_binary(6))

        

    """ 
    def delete_bomb(self, stc):
        clean_stack = Stack()
        counter = 0
        while not s.is_empty():
            element = s.pop()
            if element == "*"
    """

"""
s = Stack()
s2 = Stack()
s.push(3)
s.push(1)
s.push(4)
s.push(1)
s.push(2)
s.push(6)
func = s.even_odd(s2)
print(func[0].get_stack(), func[1].get_stack())
"""

stack = Stack()
stack.push("A")
stack.push("C")
stack.push("J")
stack.push("*")
stack.push("G")
stack.push("*")
stack.push("H")
stack.push("L")
stack.push("*")