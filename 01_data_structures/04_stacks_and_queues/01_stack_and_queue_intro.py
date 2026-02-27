# Stack:
# ------
# Stack is a linear data structure with Last-In-First-Out (LIFO) behaviour.
# E.g., Pile of papers or plates, Browser history

# Push   -  O(1)
# Pop    -  O(1)
# Peek   -  O(1)
# Lookup -  O(n)

# Stack Implementation:
# We can use either arrays or linked lists to implement a stack.
# Array:
# 1. Dynamic size with occasional copy overhead, index-based access, cache locality with contiguous memory for faster access
# 2. Push O(1), Pop O(1), Peek O(1)
# 3. Preferred for efficiency

# Linked List:
# 1. True dynamic size, linear access
# 2. Push O(1), Pop O(n), Peek O(1)
#   1. We can optimize "Pop" to O(1) using a doubly linked list. However, it would take more memory with additional operation overhead.

# Queue:
# ------
# Queue is also a linear data structure with First-In-First-Out (FIFO) behaviour.
# In case of queues, it's inefficient to use array implementation since on removing first element,
# we will need to shift all the other elements to previous indices
# E.g., Waiting list, Uber ride request, Event ticket booking process, printer order

# Push   -  O(1)
# Pop    -  O(1)
# Peek   -  O(1)
# Lookup -  O(n)

# Queue Implementation:
# We can use either arrays or linked lists to implement a queue.
# Array:
# 1. Dynamic size with occasional copy overhead, index-based access, cache locality with contiguous memory for faster access
# 2. Enqueue O(1), Dequeue O(n) [shifting indices after removing first], Peek O(1)

# Linked List:
# 1. True dynamic size, linear access
# 2. Enqueue O(1), Dequeue O(1), Peek O(1)
# 3. Preferred for efficiency
