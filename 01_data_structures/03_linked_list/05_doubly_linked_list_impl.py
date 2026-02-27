from typing import Optional

from linked_list_node import MyLinkedListNode


class MyDoublyLinkedList:
    def __init__(self, value):
        self.head = MyDoublyLinkedListNode(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):  # O(1)
        new_node = MyDoublyLinkedListNode(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

        self.length += 1

    def prepend(self, value):  # O(1)
        new_node = MyDoublyLinkedListNode(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        self.length += 1

    def insert(self, index, value):  # O(n)
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = MyDoublyLinkedListNode(value)
            previous_node_of_index = self.find_node(index - 1)
            original_node_at_index_before_insert = previous_node_of_index.next

            # Set new node's prev to previous node of index and next to original node at index before insert
            new_node.prev = previous_node_of_index
            new_node.next = original_node_at_index_before_insert

            # Set both previous node's next and original node at index before insert prev to the new node
            previous_node_of_index.next = new_node
            original_node_at_index_before_insert.prev = new_node

            self.length += 1

    def remove(self, index):  # O(n)
        if index == 0:
            # Before removing current head, set new head to the current head's next and new head's prev to None
            self.head = self.head.next
            self.head.prev = None
        elif index >= self.length - 1:  # pop
            # Before removing current tail, set new tail to the current tail's prev and new tail's prev to None
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            previous_node_of_removing_node = self.find_node(index - 1)
            node_to_remove = previous_node_of_removing_node.next
            next_node_of_removing_node = node_to_remove.next

            # Set previous node's next to the removing node's next
            previous_node_of_removing_node.next = next_node_of_removing_node

            # Set next node's prev to the removing node's prev
            next_node_of_removing_node.prev = previous_node_of_removing_node

        self.length -= 1

    def find_node(self, index):
        current_node = self.head
        current_index = 0
        while current_index <= index:
            if current_index == index:
                return current_node
            current_index += 1
            current_node = current_node.next

        return None

    def values(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def reverse(self):
        current_node = self.tail
        while current_node is not None:
            yield current_node.value
            current_node = current_node.prev

    def __str__(self):
        return str(list(self.values()))


class MyDoublyLinkedListNode(MyLinkedListNode):
    def __init__(self, value):
        super().__init__(value)
        self.prev: Optional[MyDoublyLinkedListNode] = None


doubly_linked_list = MyDoublyLinkedList(10)
doubly_linked_list.append(5)
doubly_linked_list.append(16)
print(doubly_linked_list)

doubly_linked_list.prepend(20)
doubly_linked_list.prepend(6)
print(doubly_linked_list)

doubly_linked_list.insert(0, 8)
print(doubly_linked_list)
doubly_linked_list.insert(2, 15)
print(doubly_linked_list)
doubly_linked_list.insert(3, 7)
print(doubly_linked_list)

doubly_linked_list.remove(0)
print(doubly_linked_list)
doubly_linked_list.remove(3)
print(doubly_linked_list)
doubly_linked_list.remove(2)
print(doubly_linked_list)
doubly_linked_list.remove(doubly_linked_list.length)
print(doubly_linked_list)
doubly_linked_list.remove(20)
print(doubly_linked_list)

print(list(doubly_linked_list.reverse()))
