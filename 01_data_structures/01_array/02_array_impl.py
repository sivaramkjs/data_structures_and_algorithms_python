class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):  # O(1)
        return self.data[index]

    def append(self, item):  # O(1)
        self.data[self.length] = item
        self.length += 1

    def pop(self):  # O(1)
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def remove(self, index):  # O(n)
        self.shift_items(index)  # O(n)

    def shift_items(self, index):  # O(n)
        # for current_index in self.data:
        #     if current_index > index:
        #         # shift all items after the given index by one place left
        #         self.data[current_index - 1] = self.data[current_index]

        # shift all items from the given index until the end by one place left by setting the current index to the item in the next index
        for current_index in range(index, self.length - 1):
            self.data[current_index] = self.data[current_index + 1]

        # delete the redundant last item which was already moved to its previous (left) position above
        del self.data[self.length - 1]
        self.length -= 1

    def __str__(self):
        return f"{{\n length: {self.length}, \n data: [{', '.join(f'{k}: {v}' for k, v in self.data.items())}]\n}}"


arr = MyArray()
arr.append("hi")
arr.append("hello")
arr.append("what")
arr.append("how")
arr.append("where")
print(arr.get(0))
print(arr.get(1))
# print(arr.pop())
print(arr.get(0))
print(arr)
arr.remove(2)
print(arr)
arr.append("when")
arr.remove(0)
print(arr)
