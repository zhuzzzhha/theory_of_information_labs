import heapq
import math

def huffman_coding(symbols, probabilities):
    heap = [[prob, [sym, ""]] for sym, prob in zip(symbols, probabilities)]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

symbols = ['1', '2', '3', '4', '5']
probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]

huffman_code = huffman_coding(symbols, probabilities)

for sym, code in huffman_code:
    print(f"Символ {sym}: код Хаффмана {code}")

# Вычисление характеристик кода Хаффмана

avg_length = sum(prob * len(code) for _, code, prob in zip(symbols, (code for _, code in huffman_code), probabilities))


def entropy(probabilities):
    ent = 0
    for prob in probabilities:
        if prob != 0:
            ent -= prob * math.log2(prob)
    return ent

H_max = math.log2(len(symbols))    
H = entropy(probabilities) 

redundancy = 1 - H/H_max

print(f"Избыточность: {redundancy:.1f}")
print(f"Средняя длина кодового слова: {avg_length:.1f}")

 
