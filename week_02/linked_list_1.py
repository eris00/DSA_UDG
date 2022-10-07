
class Node:

    # Constructor
    def __init__(self, value):
        # Node
        self.value = value # Data
        self.next = None # Pointer


class LinkedList:

    # Constructor
    def __init__(self, head=None):
        self.head = head

    # dodavanje elemenata na pocetak liste
    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    # print list function
    def print_list(self):
        current = self.head
        #ako lista ima elemenata
        if self.head:
            #dok next trenutnog Node-a nije None
            while current:
                print(current.value)
                current = current.next

    # dodavanje elemenata na kraj liste
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # brisanje prvog elementa sa liste
    def delete_first(self):
        # ako ne postoji head (ako je lista prazna)
        if not self.head:
            return None
        else:
            #postavimo head na naredni element tako da se prethodni automatski brise iz memorije
            self.head = self.head.next

    # brisanje posljednjeg elementa sa liste
    def delete_last(self):
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    # uzimanje vrijednosti sa neke pozicije
    def get_value_from_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None #pogresan unos..
        while current and counter <= position:
            if counter == position:
                return current #.value
            current = current.next #ako counter nije trazena pozicija prebacujemo se na naredni element
            counter = counter + 1
        return None

    # dodavanje elementa na odredjenoj poziciji
    def insert_on_position(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1: #provjeravamo je li counter stigao pred trazeni element (position)
                    new_element.next = current.next
                    current.next = new_element
                #prebacivanje elementa i pozicije naprijed
                current = current.next
                counter = counter + 1
            return None
        elif position == 1: #ako je element prvi u listi
            #radimo klasican prepend
            new_element.next = self.head
            self.head = new_element
        else:
            #pogresan unos
            return None

    # brisanje elementa po poziciji
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
                # lista ima samo jedan element
                self.head = current.next

    # brisanje elementa koji se nalazi na unijetoj poziciji
    def delete_from_position(self, position):
        current = self.head
        prev = None
        counter = 0

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

    # funkcija za racunanje duzine liste
    def len_iterative(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count = count + 1
        return count

    # rekurzvina funkcija za racunanje duzine liste
    def get_count_rec(self, node):
        #base case
        if not node:
            return 0
        else:
            #step
            return 1 + self.get_count_rec(node.next)

    def recursive_len(self):
        return self.get_count_rec(self.head)




# Creating Node
n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(6)

# Creating List
l1 = LinkedList()

#adding first element
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)

""" 
n5 = Node(11)
l1.insert_on_position(n5, 2)
l1.print_list()
"""

""" 
l1.print_list()
print('---------------')
l1.delete_first()
l1.print_list()
"""

"""
l1.print_list()
print('---------------')
l1.delete_last()
l1.print_list()
"""

""" 
print(l1.get_value_from_position(2).value) #pozicija != index
"""

""" 
l1.print_list()
l1.delete_from_position(2)
print('---')
l1.print_list()
"""

""" print(l1.len_iterative()) """

""" print(l1.recursive_len()) """