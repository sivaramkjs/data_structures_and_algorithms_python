def bin_search(a, val):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if val < a[mid]:
            high = mid - 1
        elif val > a[mid]:
            low = mid + 1
        else:
            return mid

    return -1


def bin_search_recursive(a, val, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    # print(mid)
    # print(a[low:high])

    if val < a[mid]:
        return bin_search_recursive(a, val, low, mid - 1)
    elif val > a[mid]:
        return bin_search_recursive(a, val, mid + 1, high)
    else:
        return mid


# def linear_search(a, val):
#     for i in range(0, len(a)):
#         if a[i] == val:
#             return True
#     return False

import random
from Utils.check_perf import check_performance

s = sorted([random.randrange(1, 1000) for i in range(1, 9)])
print(s)
v = random.choice(s)
print(v)
print(check_performance(bin_search_recursive, s, v, 0, len(s) - 1))
print(check_performance(bin_search, s, s[0]))
