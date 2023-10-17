# Жукова, Карякина, Хлобустова (БПМ-21-3)

import math

# энтропия 

def entropy(p):
    res = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] > 0:
                res -= p[i][j] * math.log2(p[i][j])
    
    return res/len(p[0])


# пример

p_b_given_a = [[0.9, 0.1, 0.0, 0.0], [0.05, 0.84, 0.01, 0.0], [0.03, 0.06, 0.98, 0.01], [0.02, 0.0, 0.01, 0.9]] # канальная матрица

H_b_given_a = entropy(p_b_given_a)

print(f"Энтропия: {H_b_given_a} бит/символ")
