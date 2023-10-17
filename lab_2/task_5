def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_permutation_count(elements, r):
    if r > len(elements) or r <= 0:
        return 0

    # Вычисляем количество размещений по формуле n!/(n-k)!
    num_permutations = factorial(len(elements)) // factorial(len(elements) - r)

    return num_permutations

elements = ['f1', 'f2', 'f3', 'f4']
r = 3

permutations_count = find_permutation_count(elements, r)
print(f"Количество размещений: {permutations_count}")

import math

print(f"Количество информации: {math.log(len(elements))}")


