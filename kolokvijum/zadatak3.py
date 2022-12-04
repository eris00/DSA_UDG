import statistics

class Node:
    def __init__(self, ime, ocjena):
        self.value = {'ime': ime, 'ocjena': ocjena}
        self.next = None
        self.prev = None

class LinkedList:
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
        while current:
            print(current.value['title'])
            current = current.next

    def prosjecna_ocjena(self):
        ocjene = []
        counter = 0
        current = self.head
        while current:
            ocjene.append(current.value['ocjena'])
            current = current.next
        prosjecna = statistics.mean(ocjene)
        current = self.head
        while current:
            if current.value['ocjena'] > prosjecna:
                print(current.value['ime'])
                counter += 1
            current = current.next
        print("broj ucenika koji zadovoljavaju uslov:", counter)



ucenici = LinkedList()
ucenik1 = Node('marko', 3.7)
ucenik2 = Node('janko', 5.0)
ucenik3 = Node('petar', 2.3)
ucenik4 = Node('dejan', 3.7)
ucenik5 = Node('damir', 4.2)

ucenici.append(ucenik1)
ucenici.append(ucenik2)
ucenici.append(ucenik3)
ucenici.append(ucenik4)
ucenici.append(ucenik5)

# ucenici koji zadovoljavaju uslov:
ucenici.prosjecna_ocjena()