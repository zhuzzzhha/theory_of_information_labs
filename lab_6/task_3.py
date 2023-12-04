import math

def shannon_fano_coding(probabilities):
    sorted_probs = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    codes = {char: '' for char, _ in sorted_probs}

    def recursive_divide(sub_probs):
        if len(sub_probs) <= 1:
            return

        total_prob = sum(prob for _, prob in sub_probs)
        current_sum = 0
        index = 0

        for i, (_, prob) in enumerate(sub_probs):
            if current_sum + prob <= total_prob / 2:
                current_sum += prob
                index = i
            else:
                break

        for i, (char, _) in enumerate(sub_probs):
            if i <= index:
                codes[char] += '0'
            else:
                codes[char] += '1'

        recursive_divide(sub_probs[:index + 1])
        recursive_divide(sub_probs[index + 1:])

    recursive_divide(sorted_probs)

    return codes

def entropy(probabilities):
    return -sum(prob * math.log2(prob) for prob in probabilities.values())

def average_code_length(codes, probabilities):
    return sum(len(code) * prob for code, prob in zip(codes.values(), probabilities.values()))


probabilities = {'А': 0.15, 'Б': 0.1, 'В': 0.25, 'Г': 0.13, 'Д': 0.25, 'Е': 0.12}


sf_codes = shannon_fano_coding(probabilities)

entropy_value = entropy(probabilities)

average_length_value = average_code_length(sf_codes, probabilities)

print("Символ\tВероятность\tКод Ш-Ф")
for symbol, prob in probabilities.items():
    code = sf_codes[symbol]
    print(f"{symbol}\t{prob}\t\t{code}")

print(f"\nЭнтропия: {round(entropy_value, 2)} бит")
print(f"Среднее число символов на одну букву: {round(average_length_value, 2)}")
