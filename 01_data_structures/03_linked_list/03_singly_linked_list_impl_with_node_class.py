from linked_list_node import MyLinkedListNode


class MyLinkedList:
    def __init__(self, value):
        self.head = MyLinkedListNode(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):  # O(1)
        new_node = MyLinkedListNode(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):  # O(1)
        new_node = MyLinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):  # O(n)
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = MyLinkedListNode(value)
            previous_node_of_index = self.find_node(index - 1)

            # swap new node's next to previous node's original next before insert and previous node's next to the new node
            new_node.next = previous_node_of_index.next
            previous_node_of_index.next = new_node

            self.length += 1

    def remove(self, index):  # O(n)
        if index == 0:  # Before removing current head, set new head to the current head's next node
            self.head = self.head.next
        else:
            if index >= self.length:
                index = self.length - 1  # pop

            previous_node_of_removing_node = self.find_node(index - 1)
            node_to_remove = previous_node_of_removing_node.next

            # swap previous node's next to the removing node's next, which implicitly removes the desired node from linked list
            previous_node_of_removing_node.next = node_to_remove.next

            if index == self.length - 1:  # In case of pop, set new tail to the previous node of the last node after removal
                self.tail = previous_node_of_removing_node

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
        prev_node = None
        current_node = self.head
        if not current_node.next:  # If there is only one element just return as we don't need to process anything
            return
        while current_node:
            next_node = current_node.next  # store the current node's original next
            current_node.next = prev_node  # set the current node's next to the prev node i.e., reversing
            prev_node = current_node  # move prev node to current node
            current_node = next_node  # move current node to next node
        self.head, self.tail = self.tail, self.head

    def __str__(self):
        return str(list(self.values()))


linked_list = MyLinkedList(10)
linked_list.append(5)
linked_list.append(16)
print(linked_list)

linked_list.prepend(20)
linked_list.prepend(6)
print(linked_list)

linked_list.insert(0, 8)
print(linked_list)
linked_list.insert(2, 15)
print(linked_list)
linked_list.insert(3, 7)
print(linked_list)

linked_list.remove(0)
print(linked_list)
linked_list.remove(3)
print(linked_list)
linked_list.remove(2)
print(linked_list)
linked_list.remove(20)
print(linked_list)
linked_list.remove(linked_list.length)
print(linked_list)

linked_list.reverse()
print(linked_list)
