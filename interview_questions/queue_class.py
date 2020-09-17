class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.insert(0, val)

    def dequeue(self):
        val = self.data.pop()
        return val


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
