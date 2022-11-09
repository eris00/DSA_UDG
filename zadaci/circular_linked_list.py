""" zadaci za vjezbu iz zbirke zadataka - SPA olancane liste """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def print_list(self):
        current = self.head
        if self.head:
            while current:
                print(current.value)
                current = current.next


list1 = Linked_list()
# n = int(input('How many elements you want to insert: '))
# for i in range(n):
#     elem = Node(int(input('Inset elements: ')))
#     list1.append(elem)

# elem = Node(int(input('Inset elements: ')))
# while elem != 0:
#     elem = Node(int(input('Inset elements: ')))
#     list1.append(elem)

list1.print_list()


# 1.Brojeve sa ulaza stavljati u jednostruko olančanu listu sve dok se ne unese nula, a zatim dobijenu listu ispisati na izlaz




