# Kreirati jednostruko olancanu listu - zadatak sa vjezbi

class Node:
    def __init__(self, value):
        # Node
        self.value = value # Data
        self.next = None # Pointer

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    # a) podatke unositi na pocetku liste
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # b) podatke unositi na kraju liste
    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    # c) funkcija za printanje liste
    def print_list(self):
        current = self.head
        if self.head:
            while current.next:
                print(current.value)
                current = current.next


    # d) pronalazak maksimalnog elementa u listi
    def find_max(self):
        current = self.head
        max_el = self.head.value
        while current:
            if current.value > max:
                max_el = current.value
            current = current.next
        return max_el

    # e) brisanje maksimalnog elementa
    def delete_max(self):
        current = self.head
        max_el = self.head.value
        while current:
            if current.value > max:
                max_el = current.value
            current = current.next
            self.delete_val(max_el)
            self.print_list()

    # f) kvadrirati svaki element u listi
    def square_list(self):
        current = self.head
        while current.next:
            current.value = current.value ** 2
            current = current.next

    # g) broj elemenaata liste
    def num_of_list(self):
        counter = 0
        current = self.head
        while current.next:
            counter = counter + 1
            current = current.next

    """
    # h) naci broj elemenata manjih od drugog
    def manji_od_dr_naj(self):
        current = self.head
         while current.next:
             if current.next < current:
                 current.head = self.head.next
    """

    # i) obrisati prvi element u listi
    def delete_first(self):
        if not self.head:
            return None
        else:
            self.head = self.head.next


l1 = LinkedList()

n1 = Node(2)
n2 = Node(7)
n3 = Node(4)
n4 = Node(6)

l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)








