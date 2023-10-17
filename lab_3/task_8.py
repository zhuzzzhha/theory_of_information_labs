# Жукова, Карякина, Хлобустова (БПМ-21-3)

import numpy as np
import math

# энтропия

def entropy(p):
    res = 0
    for i in range(len(p)):
        res -= p[i] * math.log2(p[i])   
    return res

def b_probabilities(p_a, p_b_given_a):
    return [sum(p_a * p_b_given_a.T[i]) for i in range(len(p_a))] # умножение по столбцам канальной матрицы

# пример использования

p_a = np.array([0.5, 0.3, 0.2]) # вероятности появления символов на входе источника

p_b_given_a = np.array([[0.97, 0.03, 0.], [0.01, 0.98, 0.01], [0., 0.04, 0.96]]) # канальная матрица

p_b = b_probabilities(p_a, p_b_given_a)

H_b_given_a = entropy(p_b)

print(f"Энтропия приемника сообщений: {H_b_given_a} бит/символ")
