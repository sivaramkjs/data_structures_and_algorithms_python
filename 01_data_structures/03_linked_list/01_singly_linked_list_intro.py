# Linked list vs Array:
# Array needs resizing every once in a while after the current memory size is exhausted, resulting in some overhead.
# Insert/delete at an index needs shifting of some elements.

# Linked list vs Hash Table:
# While hash table addressed most of the array downsides, they are not ordered.

# Linked list addresses these downsides.

# Singly Linked List:
# 1. Elements are linked from one element to next element.
# 2. Each element is called a "Node".
# 3. Each node contains the following:
#   1. Value of the element
#   2. Pointer to the next element
# 4. "Head" - First element node in the linked list.
# 5. "Tail" - Last element node in the linked list.
# 6. Linked list will always terminate with a "null" node after the tail node.

# E.g., 1-->5-->6-->null
