""" sa vjezbi za single linked list """


class Node:
    def __init__(self, value):
        self.value = value  # Data
        self.next = None  # Pointer


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def print_list(self):
        current = self.head
        if self.head:

            while current.next:
                print(current.value)
                current = current.next

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete_first(self):
        if not self.head:
            return None
        else:
            self.head = self.head.next

    def delete_last(self):
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def get_value_from_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter = counter + 1
        return None

    def insert_on_position(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter = counter + 1
            return None
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            return None

    def delete_value(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    """ 
    def delete_min(self):
        current = self.head
        min = self.head.value
        while current:
            if current.value.min
    """

    #funkcija za brisanje svakog drugog elementa
    """ 
    def brisi_drugi(self):
        current = self.head
        current2 = current.next
        while current.next:
            current2 = current.next
            current.next = current2.next
            current = current.next
    """

    #spajanje dvije liste
    def concatenate_list(self, l2):
        current = self.head
        while current.next != None:
            current.head = l2.head
        current.next = l2


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n4 = Node(4)
n5 = Node(6)
n6 = Node(9)

l1 = LinkedList()
l1.append(n1)
l1.append(n2)
l1.append(n3)

l2.append()







