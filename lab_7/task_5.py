import heapq
from collections import namedtuple

# Определяем структуру узла дерева Хаффмана
Node = namedtuple('Node', ['probability', 'symbol', 'left', 'right'])

def huffman_encoding(alphabet):
    # Создаем список узлов для каждого символа алфавита
    nodes = [Node(probability, symbol, None, None) for symbol, probability in alphabet]

    # Помещаем узлы в очередь с приоритетами
    heapq.heapify(nodes)

    # Создаем бинарное дерево Хаффмана
    while len(nodes) > 1:
        # Извлекаем два узла с наименьшими вероятностями
        node_left = heapq.heappop(nodes)
        node_right = heapq.heappop(nodes)

        # Создаем новый узел, объединяя два узла с наименьшими вероятностями
        merged_node = Node(
            probability=node_left.probability + node_right.probability,
            symbol=None,  # Новый узел не будет представлять символ
            left=node_left,
            right=node_right
        )

        # Помещаем новый узел в очередь
        heapq.heappush(nodes, merged_node)

    # Получаем корень дерева Хаффмана
    root = nodes[0]

    # Создаем словарь для хранения кодов символов
    codes = {}

    # Рекурсивно обходим дерево Хаффмана, строя коды символов
    def build_codes(node, code):
        if node.symbol is not None:
            # Добавляем код символа в словарь codes
            codes[node.symbol] = code
        else:
            # Рекурсивно обходим левое и правое поддеревья
            build_codes(node.left, code + '0')
            build_codes(node.right, code + '1')

    # Начинаем рекурсивную построение кодов символов от корня дерева
    build_codes(root, '')

    return codes

def calculate_average_length(codes, alphabet):
    # Рассчитываем среднюю длину кодов символов
    total_probability = sum(probability for _, probability in alphabet)
    average_length = sum(probability * len(codes[symbol]) for symbol, probability in alphabet) / total_probability
    return round(average_length, 3)

def calculate_optimality_factor(average_length, fixed_length):
    # Рассчитываем коэффициент оптимальности
    optimality_factor = average_length / fixed_length
    return round(optimality_factor, 3)

# Задаем алфавит - список символов с вероятностями
alphabet = [('A', 0.75), ('B', 0.1), ('C', 0.15)]

# Кодируем символы с помощью метода Хаффмана
codes = huffman_encoding(alphabet)
print("Коды символов Хаффмана:")
for symbol, code in codes.items():
    print(f'{symbol}: {code}')

# Рассчитываем среднюю длину и коэффициент оптимальности
average_length = calculate_average_length(codes, alphabet)
fixed_length = len(bin(len(alphabet)-1)[2:])  # Фиксированная длина кодов
optimality_factor = calculate_optimality_factor(average_length, fixed_length)

print("Средняя длина кодов:", average_length)
print("Коэффициент оптимальности:", optimality_factor)


# Задаем алфавит - список символов с вероятностями
alphabet = [('AA', 0.75**2), ('AB', 0.75*0.1), ('AC', 0.75*0.15), 
            ('BB', 0.1**2), ('BC', 0.1*0.15),('BA', 0.1*0.15),
            ('CC', 0.15**2),('CB', 0.1*0.15),('CA', 0.75*0.1),]

# Кодируем символы с помощью метода Хаффмана
codes = huffman_encoding(alphabet)
print("Коды двухбуквенных символов Хаффмана:")
for symbol, code in codes.items():
    print(f'{symbol}: {code}')

# Рассчитываем среднюю длину и коэффициент оптимальности
average_length = calculate_average_length(codes, alphabet)
fixed_length = len(bin(len(alphabet)-1)[2:])  # Фиксированная длина кодов
optimality_factor = calculate_optimality_factor(average_length, fixed_length)

print("Средняя длина двухбуквенных кодов:", average_length)
print("Коэффициент оптимальности двухбуквенных кодов:", optimality_factor)
 
