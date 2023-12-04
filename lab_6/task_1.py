import math

def shannon_entropy(probabilities):
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy

def redundancy(probabilities):
    entropy = shannon_entropy(probabilities)
    redundancy = 1 - entropy
    return redundancy


prob_a = 0.2
prob_b = 0.3
prob_c = 0.4
prob_d = 0.1

probabilities = [prob_a, prob_b, prob_c, prob_d]


redundancy_value = redundancy(probabilities)

print(f"Избыточность сообщений: {round(redundancy_value, 2)}")
