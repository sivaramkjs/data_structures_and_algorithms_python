from typing import Optional
from node import Node


class MyQueue:
    def __init__(self):
        self.first: Optional[Node] = None
        self.last: Optional[Node] = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        removed_value = self.safe_first_value()
        if self.length <= 1:
            self.first = self.last = None
        else:
            self.first = self.first.next

        self.length -= 1 if self.length > 0 else 0
        return removed_value

    def peek(self):
        return self.safe_first_value()

    def is_empty(self):
        return self.length == 0

    def safe_first_value(self):
        return self.first.value if self.first else None


queue = MyQueue()
queue.peek()

queue.enqueue('Siva')
print(queue.peek())
queue.enqueue('Ram')
print(queue.peek())
queue.enqueue('Sravani')
print(queue.peek())
print(queue.is_empty())

queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
print(queue.is_empty())
