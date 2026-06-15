def factorial_recursive(n):  # O(n)
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


def factorial_iterative(n):  # O(n)
    if n <= 1:
        return 1

    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


print(factorial_recursive(0))
print(factorial_iterative(10))
