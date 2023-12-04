import math

def min_code_length(messages):
    return math.ceil(math.log2(messages))

messages = [16, 128, 57, 10, 432]

for message in messages:
    binary_length = min_code_length(message)
    print(f"Для {message} сообщений в двоичном коде минимальная длина: {binary_length}")

for message in messages:
    octal_length = math.ceil(math.log2(message) / math.log2(8))
    print(f"Для {message} сообщений в восьмеричном коде минимальная длина: {octal_length}")
