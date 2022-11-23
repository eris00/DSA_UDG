class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    # dodavanje na kraja queue-a
    def enqueue(self, item):
        self.size = self.size + 1
        return self.items.append(item)

    # brisanje elementa queue-a
    def dequeue(self):
        self.size = self.size - 1
        #kada pop() prosljiedimo 0 birsemo prvi element
        return self.items.pop(0)

    # provjerava je li queue prazan
    def is_empty(self):
        return len(self.items) == 0

    # vraca prvi element iz queuea
    def first(self):
        if not self.is_empty():
            return self.items[0]

    # vraca cijeli queue
    def get_queue(self):
        return self.items

    def __len__(self):
        return self.size

q = Queue()

q.enqueue("Wake up")
q.enqueue("have a cafee")
q.enqueue("Have a shower")
q.enqueue("Get a dress")
q.enqueue("Go to breakfast")
q.enqueue("Go to university")

print(q.get_queue())
q.dequeue()

print("---")

print(q.get_queue())



