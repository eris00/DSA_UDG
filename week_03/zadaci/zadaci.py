""" zadaci Linked lista sa video predavanja """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            return None

    def delete_last(self):
        current = self.head
        prev = self.head
        if current:
            while current.next:
                prev = current
                current = current.next
            prev.next = None

    def print_list(self):
        current = self.head
        if self.head:
            while current:
                print(current.value)
                current = current.next

    def get_value_from_position(self, position):
        current = self.head
        counter = 1
        if current:
            while current and counter <= position:
                if counter == position:
                    print(current.value)
                current = current.next
                counter += 1
        else:
            return None

    def insert_on_position(self, position, new_element):
        current = self.head
        counter = 1
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
            return None
        elif position == 1:
            self.prepend(new_element)
        else:
            print('nema elemenata')

    def delete_from_position(self, position):
        current = self.head
        prev = None
        counter = 0
        if position == 1:
            self.head = current.next
            return
        while current and counter != position:
            prev = current
            current = current.next
            counter += 1
        if current is None:
            return None
        prev.next = current.next


n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n4 = Node(9)
n5 = Node(1)

list1 = LinkedList()
list1.prepend(n1)
list1.prepend(n2)
list1.prepend(n3)

list1.append(n4)
list1.append(n5)

list1.print_list()

# print('---')
# list1.delete_first()
# list1.print_list()
#
# print('---')
# list1.delete_last()
# list1.print_list()
#
# print('---')
# list1.get_value_from_position(3)

# n_new = Node(13)
# list1.insert_on_position(-1, n_new)
# print('---')
# list1.print_list()

print('---')
list1.delete_from_position(3)
list1.print_list()
