class MyLinkedList:
    def __init__(self, value):
        self.head = {'value': value, 'next': None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {'value': value, 'next': None}
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = {'value': value, 'next': self.head}
        self.head = new_node
        self.length += 1

    def values(self):
        current_node = self.head
        while current_node is not None:
            yield current_node['value']
            current_node = current_node['next']

    def __str__(self):
        return str(list(self.values()))


linked_list = MyLinkedList(10)
linked_list.append(5)
linked_list.append(16)
print(linked_list)

linked_list.prepend(20)
linked_list.prepend(6)
print(linked_list)
