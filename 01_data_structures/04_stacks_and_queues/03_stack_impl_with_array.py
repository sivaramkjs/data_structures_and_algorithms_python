class MyStackWithArray:
    def __init__(self):
        self.data = []
        # self.top = None
        # self.bottom = None

    def push(self, value):
        # if len(self.data) == 0:
        #     self.bottom = value
        self.data.append(value)
        # self.top = value

    def pop(self):
        # popped_value = self.safe_top_value()
        # if len(self.data) <= 1:
        #     self.top = self.bottom = None
        # else:
        #     del self.data[len(self.data) - 1]  # delete the old top first i.e., last element in the array
        #     self.top = self.data[len(self.data) - 1]  # set top to new last element after deletion
        #
        # return popped_value
        return self.data.pop() if len(self.data) > 0 else None

    def peek(self):
        return self.data[len(self.data) - 1] if self.data else None

    def is_empty(self):
        return len(self.data) == 0


stack = MyStackWithArray()
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
