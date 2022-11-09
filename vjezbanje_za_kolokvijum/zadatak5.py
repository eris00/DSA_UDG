class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    #find
    def find(self, value, elem):
        current = self.head
        while current:
            if current ==

    #dodavanje u listi
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    """
    def izdvoji_vece(self,value):
        counter = 0
        current = self.head
        while current:
            if current.value > value:
                counter += 1
            current = current.next
        return counter
    """
""" 
    def unija(self,l1,l2):
        pom_list = LinkedList()
        current = self.head
        while current:
            pom_list.append(l1)
            current = current.next
        current = self.head
        while current:
           if not find(current):
               pom_list.append(current)
               current = current.next
            current = current.next

return pom_list
"""



n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)

l1 = LinkedList()
l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)