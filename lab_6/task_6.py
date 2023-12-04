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
def encode_message(message):
    # Создание словаря символов и их вероятностей
    char_count = {}
    total_count = 0
    for char in message:
        char_count[char] = char_count.get(char, 0) + 1
        total_count += 1
    
    # Создание списка символов с вероятностями
    symbols = []
    for char, count in char_count.items():
        probability = count / total_count
        symbols.append(Symbol(char, probability))
    
    # Сортировка символов по убыванию вероятностей
    symbols = sorted(symbols, key=lambda symbol: symbol.probability, reverse=True)
    
    # Вызов функции разделения символов на подмножества
    shannon_fano(char_count, symbols)
    
    # Создание словаря кодов для каждого символа
    codes = {}
    for symbol in symbols:
        codes[symbol.value] = symbol.code
    
    # Кодирование сообщения
    encoded_message = ""
    for char in message:
        encoded_message += codes[char]
    
    return encoded_message, codes

# Пример использования метода Шеннона-Фано для кодирования сообщения
message = "Теория информацииКодированияМодуляции"
encoded_message, codes = encode_message(message)

print("Исходное сообщение:", message)
print("Закодированное сообщение:", encoded_message)
print("Таблица кодов:")
for char, code in codes.items():
    print(char, ":", code)
 
