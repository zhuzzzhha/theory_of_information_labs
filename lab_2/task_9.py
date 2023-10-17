# Жукова, Карякина, Хлобустова (БПМ-21-3)

import math

def equal_prob_entropy(m):

    return round(math.log2(m), 3)


# формула Шеннона для энтропии при различных вероятностях

def dif_prob_entropy(probabilities):

    info = 0

    for p in probabilities:
        info -= math.log2(p) * p
    return round(info, 3)

def underloading(h_max, h):
    return h_max - h


# пример использования

probabilities = [0.8, 0.15, 0.003, 0.015, 0.005]  # Вероятности встречаемости символов алфавита

h_max = equal_prob_entropy(len(probabilities))

h = dif_prob_entropy(probabilities)

print('Количество информации при равновероятностных символах: ', h_max)

print("Количество информации разновероятностных символах: ", h)

print('Недогруженность: ', underloading(h_max, h))
