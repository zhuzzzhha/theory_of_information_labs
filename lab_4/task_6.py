# Жукова, Карякина, Хлобустова, БПМ-21-3

import math
import numpy as np


p_a = np.array([0.2, 0.3, 0.5])

p_b_given_a= np.array([[0.97, 0.015, 0.015],
     [0.015, 0.97, 0.015],
     [0.015, 0.015, 0.97]])

# энтропия 

def entropy(prior_probabilities, channel_matrix):
    entropy = 0
    
    for i in range(len(prior_probabilities)):
        for j in range(len(channel_matrix)):
            prior_prob = prior_probabilities[i]
            conditional_prob = channel_matrix[i][j]
            
            if prior_prob != 0 and conditional_prob != 0:
                entropy += prior_prob * conditional_prob * math.log2(1 / conditional_prob)

    return entropy
    
# энтропия источника
    
H_a = -sum([p_a[i]*math.log2(p_a[i]) for i in range(len(p_a))])
    
# вероятности для приемника
    
def b_probabilities(p_a, p_b_given_a):
    return [sum(p_a * p_b_given_a.T[i]) for i in range(len(p_a))]
    
p_b = b_probabilities(p_a, p_b_given_a)

# энтропия приемника

H_b =  -sum([p_b[i]*math.log2(p_b[i]) for i in range(len(p_b))])

#условная энтропия
H_b_given_a = entropy(p_a, p_b_given_a)


info =  H_b - H_b_given_a

print(f"Количество информации: {round(info, 3)} бит")
