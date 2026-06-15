def fibonacci_bottom_up_1(n):
    if n < 2:
        return n

    fibs = [0, 1]

    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[n]


def fibonacci_bottom_up_2(n):  # O(1) space complexity
    if n < 2:
        return n

    prev_2 = 0
    prev_1 = 1
    fib = 1

    for i in range(2, n + 1):
        fib = prev_1 + prev_2
        prev_2, prev_1 = prev_1, fib

    return fib


# print(fibonacci_bottom_up_1(0))
# print(fibonacci_bottom_up_1(2))
# print(fibonacci_bottom_up_1(3))
# print(fibonacci_bottom_up_1(30))
#
# print(fibonacci_bottom_up_2(0))
# print(fibonacci_bottom_up_2(2))
# print(fibonacci_bottom_up_2(3))
# print(fibonacci_bottom_up_2(30))


def fibonacci_top_down(n, fibs: list = None):
    if fibs is None:
        fibs = [0, 1]

    if n < len(fibs):
        # print(f'cache - {n}')
        return fibs[n]

    fibs.append(fibonacci_top_down(n - 1, fibs) + fibonacci_top_down(n - 2, fibs))
    # print(f'calc - {n}')

    return fibs[n]


print(fibonacci_top_down(0))
print(fibonacci_top_down(5))
print(fibonacci_top_down(3))
print(fibonacci_top_down(30))
