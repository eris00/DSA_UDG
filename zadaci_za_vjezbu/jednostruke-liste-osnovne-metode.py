class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_lists:
    def __init__(self, head = None):
        self.head = head

    # dodavanje na pocetak liste
    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    #dodavanje na kraj liste
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # stampa liste
    def print_list(self):
        current = self.head
        if self.head:
            while current:
                print(current.value)
                current = current.next
        else:
            print('list is empty!')

    # izbrisi prvi
    def delete_first(self):
        if self.head:
           self.head = self.head.next
        else:
            return None

    # izbrisi zadnji
    def delete_last(self):
        current = self.head
        prev = self.head
        if self.head:
            while current.next:
                prev = current
                current = current.next
            prev.next = None
        else:
            print('No list')

    # izbrisi element sa pozciije
    def delete_from_position(self, position):
        if position < 1:
            return None
        i = 1
        current = self.head
        prev = None
        if self.head:
            while i != position:
                i += 1
                prev = current
                current = current.next
            prev.next = current.next
        else:
            print('no list')

    # izmijeni element na poziciju
    def update_in_position(self, position, val):
        if position < 1:
            return None
        i = 1
        current = self.head
        if self.head:
            while current and i != position:
                i += 1
                current = current.next
            current.value = val
        else:
            print('No list')

    # vrati element sa pozicije
    def get_from_position(self, position):
        if position < 1:
            return None
        i = 1
        current = self.head
        if self.head:
            while current and i != position:
                i += 1
                current = current.next
            print(current.value)
        else:
            print('No list')

    # ubaci element na poziciju
    def insert_in_position(self, position, new_element):
        if position < 1:
            return None
        current = self.head
        if self.head:
            while current != position:
                current = current.next
            new_element.next = current.next
            current.next = new_element

    # vrati duzinu liste
    def len_of_list(self):
        i = 0
        current = self.head
        if self.head:
            while current:
                current = current.next
                i += 1
            return i
        else:
            print('No elements in list')

    # naci najmanji broj u listi
    def min_element(self):
        current = self.head
        min_elem = current.value
        if self.head:
            while current:
                if current.value < min_elem:
                    min_elem = current.value
                current = current.next
            return min_elem

    # brisi svaki drugi element iz liste #! ! !
    def delete_svaki_drugi(self):
        current = self.head
        current2 = current.next
        while current.next:
            current_2 = current.next
            current.next = current_2.next
            current = current.next



list1 = Linked_lists()

el1 = Node(2)
el2 = Node(4)
el3 = Node(3)
el4 = Node(6)
el5 = Node(8)
el6 = Node(9)

list1.append(el1)
list1.append(el2)
list1.append(el3)
list1.append(el4)
list1.append(el5)
list1.append(el6)

list1.print_list()
print('--- --- ---')

list1.delete_svaki_drugi()











