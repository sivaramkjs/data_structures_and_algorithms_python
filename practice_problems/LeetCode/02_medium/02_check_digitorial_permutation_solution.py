def is_digitorial_permutation(n: int) -> bool:
    # input is a positive integer
    # output is true or false
    # permutation must not start with zero, but can be present at any other position in the number
    permutations = set()
    permute(str(n), results=permutations)

    for permutation in permutations:
        fact = 0
        for num in permutation:
            fact += factorial(int(num))
        if fact == int(permutation):
            return True

    return False


def permute(digits, path='', used=set(), results=set()):
    if len(path) == len(digits):
        if path[0] != '0':
            results.add(path)
        return
    for i, d in enumerate(digits):
        if i not in used:
            used.add(i)
            permute(digits, path + d, used, results)
            used.remove(i)  # Backtrack: unpick


# def get_digits(n):
#     digits = []
#     quotient = n // 10
#     remainder = n % 10
#     while quotient >= 10:
#         digits.append(remainder)
#         remainder = quotient % 10
#         quotient = quotient // 10
#     else:
#         digits.append(remainder)
#         digits.append(quotient)
#
#     return digits


def factorial(n):
    if n <= 1:
        return 1

    facts = [1, 1]
    for i in range(2, n + 1):
        facts.append(i * facts[i - 1])

    return facts[n]


# print(factorial(0))
# print(get_digits(123456789))
print(is_digitorial_permutation(415))
