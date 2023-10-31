# Жукова, Карякина, Хлобустова, БПМ-21-3

import math
import numpy as np


p_a = np.array([1/3]*3)

p_b_given_a= np.array([[0.95, 0.025, 0.025],
     [0.025, 0.95, 0.025],
     [0.025, 0.025, 0.95]])


def entropy(p):
    res = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] > 0:
                res -= p[i][j] * math.log2(p[i][j])
                
    return res/len(p[0])
    
def b_probabilities(p_a, p_b_given_a):
    return [sum(p_a * p_b_given_a.T[i]) for i in range(len(p_a))]
    
H_a = -sum([p_a[i]*math.log2(p_a[i]) for i in range(len(p_a))])


p_b = b_probabilities(p_a, p_b_given_a)
H_b =  -sum([p_b[i]*math.log2(p_b[i]) for i in range(len(p_b))])
H_b_given_a = entropy(p_b_given_a)

H_ab = H_a + H_b_given_a


info = H_a + H_b - H_ab
print(f"Количество информации: {round(info, 3)} бит")
