import math

# Вероятности символов
p1 = 0.2
p2 = 0.7
p3 = 0.1

# Частота тактовых импульсов генератора в герцах
F = 500  # 500 Гц

# Энтропия
H_X = - sum(p * math.log2(p) for p in [p1, p2, p3])

# Длины кодовых слов для равномерного двоичного кода
l1 = l2 = l3 = 1

# Средняя длина кодового слова
L = sum(p * l for p, l in zip([p1, p2, p3], [l1, l2, l3]))

# Пропускная способность
C = H_X * F

# Количество различных символов в алфавите
M = 3

# Скорость передачи информации
R = C * math.log2(M)

print(f"Энтропия: {round(H_X, 2)} бит")
print(f"Пропускная способность: {round(C, 2)} бит/с")
print(f"Средняя длина кодового слова: {round(L, 2)} бит")
print(f"Скорость передачи информации: {round(R, 2)} бит/с")
