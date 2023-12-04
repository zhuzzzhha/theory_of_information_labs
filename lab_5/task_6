import math

letter_probs = {'a': 0.081, 'b': 0.014, 'c': 0.027, 'd': 0.038, 
                'e': 0.13, 'f': 0.029, 'g': 0.02, 'h': 0.052, 
                'i': 0.063, 'j': 0.00013, 'k': 0.004, 'l': 0.034, 
                'm': 0.025, 'n': 0.071, 'o': 0.079, 'p': 0.019, 
                'q': 0.00011, 'r': 0.068, 's': 0.061, 't': 0.105, 
                'u': 0.024, 'v': 0.009, 'w': 0.015, 'x': 0.00015, 
                'y': 0.019, 'z': 0.0007}

duration_dict = {'e': 10, 't': 10, 'o': 10, 'n': 10, 'a': 20, 'b': 20, 
                'c': 20, 'd': 20, 'f': 20, 'g': 20, 'h': 20, 'i': 20, 
                'j': 20, 'k': 20, 'l': 20, 'm': 20, 'p': 20, 'q': 20, 
                'r': 20, 's': 20, 'u': 20, 'v': 20, 'w': 20, 'x': 20, 
                'y': 20, 'z': 20}

transmission_speed = 0

for letter, prob in letter_probs.items():
    transmission_speed -= prob * math.log2(prob) / (duration_dict[letter]*0.001*prob)
    
print(f"Скорость передачи информации: { round(transmission_speed, 2)} бит/сек")
