""" zadaci za vjezbu iz zbirke zadataka - SPA olancane liste """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, new_node):
        current = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            new_node.next = new_node

    def print_list(self):
        current = self.head
        if self.head:
            while current:
                print(current.value)
                current = current.next
                if current == self.head:
                    break

    def delete_last(self):
        current = self.head
        prev = None
        if current:
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head
        else:
            self.head = None

    def delete_first(self):
        current = self.head
        if self.head:
            while current.next != self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head



list1 = Linked_list()

e1 = Node(5)
e2 = Node(6)
e3 = Node(1)
e4 = Node(7)
e5 = Node(14)
e6 = Node(11)

list1.append(e1)
list1.append(e2)
list1.append(e3)
list1.append(e4)
list1.append(e5)
list1.append(e6)

list1.print_list()

print('---')
list1.delete_first()
list1.print_list()