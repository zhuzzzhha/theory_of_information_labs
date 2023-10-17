import math
def conditional_entropy(probabilities):
    entropy = 0
    for p in probabilities:
        if p != 0:
            print(p)
            entropy -= p * math.log2(p)
    return entropy

# Дано
total_messages = 100
count_K = 50
count_T = 30
count_K_and_T = 10

p_K = count_K/total_messages
p_T = count_T/total_messages

p_K_and_T = count_K_and_T/total_messages

p_K_cond_T = p_K_and_T/p_T
p_T_cond_K = p_K_and_T/p_K


H_K_given_T = conditional_entropy([p_K_cond_T])
H_T_given_K = conditional_entropy([p_T_cond_K])


print(f"Условная энтропия H(K|T) = {H_K_given_T}")
print(f"Условная энтропия H(T|K) = {H_T_given_K}")
