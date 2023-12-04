# Определение класса для символа
class Symbol:
    def __init__(self, value, probability, code=""):
        self.value = value
        self.probability = probability
        self.code = code

# Рекурсивная функция для разделения символов на подмножества
def shannon_fano(codes, symbols):
    if len(symbols) >= 2:
        total_prob = sum(symbol.probability for symbol in symbols)
        mid_prob = 0
        mid = 0
        for i, symbol in enumerate(symbols):
            mid_prob += symbol.probability
            if mid_prob >= total_prob / 2:
                mid = i
                break
        
        for i in range(len(symbols)):
            if i <= mid:
                symbols[i].code += "0"
            else:
                symbols[i].code += "1"
        
        shannon_fano(codes, symbols[:mid+1])
        shannon_fano(codes, symbols[mid+1:])

# Функция для кодирования сообщения
def encode_message(message, codes):
    encoded_message = ""
    for char in message:
        encoded_message += codes[char]
    
    return encoded_message

# Функция для декодирования сообщения
def decode_message(encoded_message, codes):
    decoded_message = ""
    code = ""
    for bit in encoded_message:
        code += bit
        for char, char_code in codes.items():
            if code == char_code:
                decoded_message += char
                code = ""
                break
    
    return decoded_message

# Список символов и их вероятности
symbols = [
    Symbol("A", 0.1),
    Symbol("B", 0.2),
    Symbol("C", 0.05),
    Symbol("D", 0.3),
    Symbol("E", 0.05),
    Symbol("F", 0.15),
    Symbol("G", 0.15)
]

# Сортировка символов по убыванию вероятностей
symbols = sorted(symbols, key=lambda symbol: symbol.probability, reverse=True)

# Вызов функции разделения символов на подмножества
shannon_fano({}, symbols)

# Создание словаря кодов для каждого символа
codes = {}
for symbol in symbols:
    codes[symbol.value] = symbol.code

# Построение кода Шеннона-Фано
print("Коды Шеннона-Фано:")
for char, code in codes.items():
    print(char, ":", code)

# Расчет среднего количества разрядов на одну букву
total_bits = round(sum(len(symbol.code) * symbol.probability for symbol in symbols), 2)
print("Среднее количество разрядов на одну букву:", total_bits)

# Декодирование последовательности
encoded_message = "10011101001000111101110101111000"
decoded_message = decode_message(encoded_message, codes)
print("Декодированное сообщение:", decoded_message)
 
