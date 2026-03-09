# Given a number N return the value of the Fibonacci sequence at index N, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8

def fibonacci_iterative(n):  # O(n)
    if n < 2:
        return n
    # Space Complexity: O(1)
    # fib_prev_2 = 1
    # fib_prev_1 = 1
    # fib = 1
    # for i in range(3, n + 1):
    #     fib = fib_prev_1 + fib_prev_2
    #     fib_prev_1, fib_prev_2 = fib, fib_prev_1

    # Space Complexity: O(n)
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def fibonacci_recursive(n):  # O(2^n)
    if n < 2:
        return n

    # Each recursion results in 2 * O(1) calls growing exponentially with each further recursion. Hence, 2^n * (1) = O(2^n)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_iterative(8))
# print(fibonacci_recursive(6))
