""" napraviti novu listu od liste ciji su elementi desno pozitivni a lijevo negativni"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    #dodavanje u listi
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # brisanje sa pozicije
    def delete_from_position(self, position):
        current = self.head
        prev = None
        counter = 1

        if position == 1:
            self.head = current.next
            current = None
            return

        while current and counter != position:
            prev = current
            current = current.next
            counter = counter + 1

        if current is None:
            return None

        prev.next = current.next
        current = None

    #napraviti find funkciju..

    def main_fun(self, position):
        negative_list = LinkedList()
        positive_list = LinkedList()
        zero_list = LinkedList()
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if current < 0:
                negative_list.append(current)
            elif current > 0:
                positive_list.append(current)
            else:
                zero_list.append(current)

            current = current.next
            counter = counter + 1
        return None

n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)

l1 = LinkedList()
l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)