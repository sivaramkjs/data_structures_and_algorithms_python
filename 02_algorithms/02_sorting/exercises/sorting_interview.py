# 1 - Sort 10 schools around your house by distance: Insertion sort (small input)

# 2 - eBay sorts listings by the current Bid amount: Radix/counting sort (since bid amounts are fixed range numbers.
#                                                    However, need to be mindful about floating point numbers in which case, quick/heap sort)

# 3 - Sport scores on ESPN: Quick/Heap sort (Due to different types of sport data scores and better space complexity)

# 4 - Massive database (can't fit all into memory) needs to sort through past year's user data
#       "Merge sort" (since we will need to sort externally out-of-memory, and also it can be based on random user data
#       type. Due to these variables, it may risk worst case O(n^2) with "quick sort".
#       Additionally, as this will be external sorting, "heap sort" may not be efficient since it does in-place sort with
#       array random access, which will be slower with disk I/O)

# 5 - Almost sorted Udemy review data needs to update and add 2 new reviews: Insertion sort (almost sorted data)

# 6 - Temperature Records for the past 50 years in Canada:
#       Radix/Counting sort if temperatures doesn't have decimal points since the actual range of values is limited.
#       Quick sort (For better space complexity and values are not very random)

# 7 - Large username database needs to be sorted. Data is very random: Merge/Quick sort (since data is random, it may risk quick sort worst case)

# 8 - You want to teach sorting for the first time: Bubble sort (easy and natural way to understand sorting)
