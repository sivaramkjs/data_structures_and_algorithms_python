class CustomHeap:
    @staticmethod
    def build_max_heap(data: list):
        last_non_leaf_node_index = (len(data) - 1) // 2
        for i in range(last_non_leaf_node_index, -1, -1):
            CustomHeap.max_heapify(data, i, len(data))

        return data

    @staticmethod
    def max_heapify(data: list, i, heap_size):
        while True:
            left_child_index = (2 * i) + 1
            right_child_index = (2 * i) + 2
           
            largest_index = i
            if left_child_index < heap_size and data[left_child_index] > data[largest_index]:
                largest_index = left_child_index
            if right_child_index < heap_size and data[right_child_index] > data[largest_index]:
                largest_index = right_child_index

            if largest_index == i:
                break

            data[i], data[largest_index] = data[largest_index], data[i]
            i = largest_index
