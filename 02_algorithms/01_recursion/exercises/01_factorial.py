def factorial_recursive(n):  # O(n)
    if n == 2:
        return n

    return n * factorial_recursive(n - 1)


def factorial_iterative(n):  # O(n)
    if n == 1 or n == 2:
        return n

    fact = 2
    for i in range(3, n + 1):
        fact *= i
    return fact


print(factorial_recursive(10))
print(factorial_iterative(10))
