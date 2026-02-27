# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Assumptions:
# 1. Push value will always be a positive integer between 1 and 9.
# 2. Pop and peek calls are always made when there is at least 1 element in the queue.

# Approach 1:
# 1. We can use one active stack and one temp stack.
# 2. Active stack holds the elements in the final queue order. Temp stack is used to move the elements to and fro between active stack to maintain the queue order.
# 3. During push operation,
#   1. Pop all elements from active stack and push them in the reverse queue order into temp stack.
#   2. Push the current incoming element into active stack.
#   3. Pop all elements from temp stack and push them in the reverse (final queue) order into temp stack.
# 4. Use active stack for all queue operations.
# Time Complexity:
#   Push - O(n)
#   Pop - O(1)
#   Peek - O(1)
# Space Complexity: O(n)

class MyQueueUsingStack:
    def __init__(self):
        self.active_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        while self.active_stack:
            popped_val = self.active_stack.pop()
            self.temp_stack.append(popped_val)

        self.active_stack.append(x)

        while self.temp_stack:
            temp_popped_val = self.temp_stack.pop()
            self.active_stack.append(temp_popped_val)

    def pop(self) -> int:
        return self.active_stack.pop()

    def peek(self) -> int:
        return self.active_stack[len(self.active_stack) - 1]

    def empty(self) -> bool:
        return len(self.active_stack) == 0


# obj = MyQueueUsingStack()
# obj.push(1)
# obj.push(2)
# print(obj.peek())
# print(obj.pop())
# print(obj.empty())


# Optimized approach:
# 1. Maintain separate input stack and output stack.
# 2. Push into input stack.
# 3. Pop from output stack,
#   1. If output stack is empty then move all elements from input stack to output stack, which will maintain the final queue order (i.e., reverse input stack order).
#   2. As long as output stack is not empty then all elements in it are in the final queue order and are available to pop/peek.
#   3. Alternatively, we can also keep the same moving logic in the push method.
# Time Complexity:
#   Push - O(1)
#   Pop/Peek - Amortized O(1), since move from input to output would take O(n) occasionally when the pop/peek is called and output stack is empty. Hence, O(n)/n ≈ O(1)
# Space Complexity: O(n)

class MyQueueUsingStackAmortized:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self.transfer_input_to_output()
        return self.output_stack.pop()

    def peek(self) -> int:
        self.transfer_input_to_output()
        return self.output_stack[len(self.output_stack) - 1]

    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def transfer_input_to_output(self):
        if not self.output_stack:
            while self.input_stack:
                popped_val = self.input_stack.pop()
                self.output_stack.append(popped_val)


obj = MyQueueUsingStackAmortized()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
