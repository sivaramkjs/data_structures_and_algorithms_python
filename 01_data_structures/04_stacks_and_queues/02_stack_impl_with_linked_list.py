from typing import Optional
from node import Node


class MyStack:
    def __init__(self):
        self.top: Optional[Node] = None
        self.bottom: Optional[Node] = None
        self.length = 0

    def push(self, value):
        if self.length == 0:
            self.top = self.bottom = Node(value)
        else:
            old_top = self.top
            self.top = Node(value)
            self.top.next = old_top

        self.length += 1

    def pop(self):
        popped_value = self.safe_top_value()
        if self.length <= 1:
            self.top = self.bottom = None
        else:
            self.top = self.top.next

        self.length -= 1 if self.length > 0 else 0
        return popped_value

    def peek(self):
        return self.safe_top_value()

    def is_empty(self):
        return self.length == 0

    def safe_top_value(self):
        return self.top.value if self.top else None


stack = MyStack()
print(stack.pop())

stack.push('Google')
print(stack.peek())
stack.push('Udemy')
print(stack.peek())
stack.push('Discord')
print(stack.peek())
print(stack.is_empty())

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.peek())

print(stack.pop())

print(stack.is_empty())
