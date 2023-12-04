# Жукова, Карякина (БПМ-21-3)

import numpy as np
import math

# энтропия

def entropy(p):
    res = 0
    for i in range(len(p)):
        res -= p[i] * math.log2(p[i])   
    return res
    
# условная энтропия
    
def cond_entropy(prior_probabilities, channel_matrix):

    entropy = 0
    
    for i in range(len(prior_probabilities)):
        for j in range(len(channel_matrix)):
            prior_prob = prior_probabilities[i]
            conditional_prob = channel_matrix[i][j]
            
            if prior_prob != 0 and conditional_prob != 0:
                entropy += prior_prob * conditional_prob * math.log2(1 / conditional_prob)

    return entropy


# пример использования

p_x = np.array([0.5, 0.25, 0.125, 0.125]) # вероятности появления символов на входе источника

p = np.array([[13/16, 3/16, 0., 0.], [1/8, 1/2, 3/8, 0.], [0., 0., 0., 1.], [1/2, 1/4, 1/4, 0.]]) # канальная матрица

H1 = entropy(p_x) # энтропия без учета статистической связи

H_max = math.log2(len(p_x)) # энтропия с учетом статистической связи

H2 = cond_entropy(p_x, p)

# избыточность

R1 = 1 - H1/H_max

R2 = 1 - H2/H_max

print(f'Избыточность без учета статистической связи: {R1:.3f}')

print(f'Избыточность с учетом статистической связи: {R2:.3f}')
