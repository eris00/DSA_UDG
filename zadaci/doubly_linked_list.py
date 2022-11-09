class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def prepend(self, new_element):
        if self.head is None:
            self.head = new_element
        else:
            new_element.next = self.head
            self.head.prev = new_element
            self.head = new_element

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            new_element.prev = current
        else:
            self.head = new_element

    def delete_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        self.head = self.head.next
        self.prev = None

    def delete_last(self):
        current = self.head
        before_last = None
        if self.head:
            while current.next:
                before_last = current
                current = current.next
            before_last.next = None

    def delete_last_two(self):
        current = self.head
        while current.next:
            current = current.next
        current.prev.prev.next = None

    # izbaciti N zadnjih elemenata iz liste
    def remove_n_last(self, n):
        current = self.head
        counter = 0
        while current.next:
            current = current.next
        while counter < n:
            current = current.prev
            counter += 1
        current.next = None

    # uzmi srednju vrijednost
    def get_middle_node(self):
        current_1 = self.head
        current_2 = self.head
        while current_1.next:
            current_1 = current_1.next.next
            current_2 = current_2.next
        print(current_2.value)

    #jesu li dvije liste identicne
    def __eq__(self, other):
        current_1 = self.head
        current_2 = other.head
        while current_1 and current_2:
            if current_1.value == current_2.value:
                current_1 = current_1.next
                current_2 = current_2.next
            else:
                return False
        if not current_1 and not current_2:
            return True
        else:
            return False

    def insert_at_position(self, position, inserted_value):
        current = self.head
        counter = 1
        if self.head:
            while current:
                if counter == position:
                    current.value = inserted_value
                current = current.next
                counter += 1

    def delete_el_by_value(self, inserted_value):
        current = self.head
        while current:
            if current.value == inserted_value:
                current.prev.next = current.next
                current.next.prev = current.prev
            current = current.next

    def reverse(self):
        current = self.head
        while current.next:
            current = current.next
        while current != self.head:
            print(current.value)
            current = current.prev

    def concat(self, second):
        current_1 = self.head
        current_2 = second.head
        while current_1.next:
            current_1 = current_1.next
        current_1.next = second.head


list1 = DoublyLinkedList()
el1 = Node(1)
el2 = Node(2)
el3 = Node(3)
el4 = Node(4)
el5 = Node(5)
list1.append(el1)
list1.append(el2)
list1.append(el3)
list1.append(el4)
list1.append(el5)

list2 = DoublyLinkedList()
sl1 = Node(4)
sl2 = Node(4)
sl3 = Node(4)
list2.append(sl1)
list2.append(sl2)
list2.append(sl3)

list1.print_list()
print('---')

list1.print_list()