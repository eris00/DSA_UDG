class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly_linked_list:
    def __init__(self, head = None):
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

    def delete_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        self.head = self.head.next
        self.prev = None

    # izbaciti N zadnjih elemenata iz liste



    # uzmi srednju vrijednost



    #jesu li dvije liste identicne eq



    # append, delete_last, delete_first, delete_last_two, insert_at_position, delete_element_by_value, reverse, concat
