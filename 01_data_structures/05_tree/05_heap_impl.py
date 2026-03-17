import heapq


class MyHeap:
    @staticmethod
    def build_max_heap(data: list):  # O(n log n)
        # 1. Start from last non-leaf node and fix max heap property until the root node.
        # 2. In any complete binary tree represented with a 0-based index list/array, for any node at index "i", the left and right children will be at the following indices.
        #   1. left child - 2i+1
        #   2. right child - 2i+2
        # 3. If the binary tree array length is "n" then the last non-leaf node must be at "(n-1)/2" since
        #   1. For any node, if its left child index 2i+1 > n then the node must be a leaf node since there are no children.
        #   2. Hence, the largest valid index i for which 2i+1 <= n --> i <= (n-1)/2.

        last_non_leaf_node_index = (len(data) - 1) // 2
        for i in range(last_non_leaf_node_index, -1, -1):
            MyHeap.__max_heapify(data, i)

        return data

    @staticmethod
    def __max_heapify(data: list, i):
        # 1. In any complete binary tree represented with a 0-based index list/array, for any node at index "i", the left and right children will be at the following indices.
        #   1. left child - 2i+1
        #   2. right child - 2i+2
        # 2. Loop while true.
        # 3. Set largest to i.
        # 3. Compare the current node with its left child.
        #   1. If "left child index < heap_size" and "node[i] < left" then set largest to left child node index.
        # 4. Compare the largest index node from step 3 with the right child.
        #   1. If "right child index < heap_size" and "node[largest] < right" then set largest to right child node index.
        # 5. Compare largest is the current node index (i).
        #   1. If they are equal then end the loop as we don't need to heapify the child subtrees.
        #       1. This works properly as when the current node is already greater than its child nodes then we can assume that the child subtrees are already valid heaps. This is due to the fact how we build the heap bottom up from the last non-leaf node.
        #   2. Else swap current node with the child node at the largest index.
        # 6. Set i = largest.
        # 7. Repeat steps 3 to 6.

        heap_size = len(data)

        while True:
            left_child_index = (2 * i) + 1
            right_child_index = (2 * i) + 2
            # print(
            #     f'node: {data[i]}, left: {data[left_child_index] if left_child_index < self.heap_size else None}, right: {data[right_child_index] if right_child_index < self.heap_size else None}')

            largest_index = i
            if left_child_index < heap_size and data[left_child_index] > data[largest_index]:
                largest_index = left_child_index
            if right_child_index < heap_size and data[right_child_index] > data[largest_index]:
                largest_index = right_child_index

            if largest_index == i:
                break

            data[i], data[largest_index] = data[largest_index], data[i]
            i = largest_index

    @staticmethod
    def max_heap_insert(data, value):  # O(log n)
        # 1. Set new node index to the current largest index + 1 (= len(data), for a 0-based index list/array) before adding the new node.
        # 2. Add the new value into the list.
        # 3. Compute the parent node index of the new node.
        #   1. 1st (left) child node index = (2 * parent node index) + 1 => parent node index = (child node index - 1) // 2
        # 4. Fix the heap property by bubbling up from the new node to the root.
        # 5. Set current index to the new node index.
        # 6. Loop while current index > 0 (until root node) and parent node < current node.
        # 7. Swap parent node with current node.
        # 8. Set current index = parent node index.
        # 9. Compute the parent node index of the current index.
        # 10. Repeat steps 6- 7

        new_node_index = len(data)
        data.append(value)

        compute_parent_node_index = lambda index: (index - 1) // 2
        current_node_index = new_node_index
        parent_node_index = compute_parent_node_index(current_node_index)

        while current_node_index > 0 and data[parent_node_index] < data[current_node_index]:
            data[parent_node_index], data[current_node_index] = data[current_node_index], data[parent_node_index]
            current_node_index = parent_node_index
            parent_node_index = compute_parent_node_index(current_node_index)

    @staticmethod
    def extract_max(data):  # O(log n)
        # 1. Get the max value from the root node at the first index.
        # 2. Replace the root node with the last leaf node from the last index.
        # 3. Fix the heap property from the new root (bubbling down).
        max_val = data[0]
        data[0] = data[len(data) - 1]
        data.pop()
        MyHeap.__max_heapify(data, 0)
        return max_val


print(MyHeap.build_max_heap([1, 3, 4, 2, 5]))
d = [74, 3, 26, 83, 98, 18, 81, 65, 96, 82]
MyHeap.build_max_heap(d)
print(d)
MyHeap.max_heap_insert(d, 100)
print(d)
MyHeap.extract_max(d)
print(d)
print('\n')
d1 = [74, 3, 26, 83, 98, 18, 81, 65, 96, 82]
heapq.heapify_max(d1)
print(d1)
heapq.heappush_max(d1, 100)
print(d1)
heapq.heappop_max(d1)
print(d1)
