import math
def conditional_entropy(prob, cond_prob):
    entropy = -prob * cond_prob * math.log2(prob)
    return entropy

# Дано
p_A = 0.6
p_B = 0.4

p_B_cond_A = 0.15
p_A_cond_B = 0.1


H_A_B = conditional_entropy(p_B,p_A_cond_B)

print(f"Условная энтропия H(K|T) = {H_A_B}")
