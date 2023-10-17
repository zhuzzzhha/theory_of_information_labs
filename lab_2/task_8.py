# Жукова, Карякина, Хлобустова (БПМ-21-3)

import math

# формула Шеннона для энтропии при различных вероятностях

def entropy(probabilities):

    info = 0

    for p in probabilities:
        info -= math.log2(p) * p
    return round(info, 3)


# пример использования

probabilities = [0.25, 0.25, 0.32, 0.16]  # Вероятности встречаемости символов алфавита


print("Количество информации:", entropy(probabilities))
