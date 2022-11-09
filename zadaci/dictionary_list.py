import statistics

class Node:
    def __init__(self, title, genre, year, rate):
        self.value = {'title': title, 'genre': genre, 'year': year, 'rate': rate}
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

    def average_rate(self):
        rates = []
        current = self.head
        while current:
            rates.append(current.value['rate'])
            current = current.next
        print(statistics.mean(rates))

    # svi filmovi nakon unijete godine
    def from_year(self, year):
        current = self.head
        while current:
            if current.value['year'] >= year:
                print(current.value['title'])
            current = current.next

    # koliko filmova ima zadati zanr
    def all_from_genre(self, genre):
        counter = 0
        current = self.head
        while current:
            if current.value['genre'] == genre:
                counter += 1
            current = current.next
        return counter



list1 = LinkedList()
movie1 = Node('film1', 'comedy', 2016, 6.2)
movie2 = Node('film2', 'fantasy', 2021, 5.7)
movie3 = Node('film3', 'history', 2008, 8.0)
movie4 = Node('film2', 'fantasy', 2022, 9.0)
movie5 = Node('film2', 'fantasy', 1993, 6.7)

list1.append(movie1)
list1.append(movie2)
list1.append(movie3)
list1.append(movie4)
list1.append(movie5)

list1.all_from_genre('fantasy')