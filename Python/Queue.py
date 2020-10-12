class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
test = Queue()
second_q= Queue()
test.enqueue("testing string")
test.enqueue("item number 2")
test.enqueue("different")
test.enqueue("testing a queue")
print(test.queue)
print(second_q.enqueue(test.dequeue()))
print('1',second_q.queue)
print(test.queue)