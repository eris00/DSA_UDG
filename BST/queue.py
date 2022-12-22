class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def peek(self):
        if len(self.items) > 0:
            return self.items[0].value
    
    def __len__(self):
        return len(self.items)

# q = Queue()

# q.enqueue("Wake up")
# q.enqueue("have a cafee")
# q.enqueue("Have a shower")
# q.enqueue("Get a dress")
# q.enqueue("Go to breakfast")
# q.enqueue("Go to university")

# print(q.get_queue())
# q.dequeue()

# print("---")

# print(q.get_queue())



