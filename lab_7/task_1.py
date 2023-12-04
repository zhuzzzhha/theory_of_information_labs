import heapq
from collections import defaultdict

def huffman_coding(probabilities):
    heap = [[weight, [char, ""]] for char, weight in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0][1:]

def huffman_characteristics(codes):
    average_code_length = sum(len(code[1]) for code in codes) / len(codes)
    entropy = sum(prob * len(code[1]) for prob, code in zip(probabilities.values(), codes))
    efficiency = entropy / average_code_length
    return average_code_length, entropy, efficiency

# Вероятности появления символов
probabilities = {'x1': 0.25, 'x2': 0.25, 'x3': 0.125, 'x4': 0.125, 'x5': 0.0625, 'x6': 0.0625, 'x7': 0.0625, 'x8': 0.0625}

# Построение кода Хаффмана
huffman_codes = huffman_coding(probabilities)

# Определение характеристик кода
avg_length, entropy, efficiency = huffman_characteristics(huffman_codes)

# Вывод результатов
print("Символ\tВероятность\tКод Хаффмана")
for symbol, prob in probabilities.items():
    code = next(code[1] for code in huffman_codes if code[0] == symbol)
    print(f"{symbol}\t{prob}\t\t{code}")

print(f"\nСредняя длина кодового слова: {avg_length}")
print(f"Энтропия: {entropy}")
print(f"Эффективность кода: {round(efficiency, 2)}")
