import math


p_a = [0.25, 0.25, 0.5]

P = [[0.97, 0.015, 0.015],
     [0.02, 0.97, 0.01],
     [0.01, 0.01, 0.98]]

H_X_given_Y = 0


for a in range(len(P)):
    for b in range(len(P[0])):
        if P[a][b] != 0:
            H_X_given_Y += p_a[a] * P[a][b] * math.log2(1 / P[a][b])


H_X = sum([-p * math.log2(p) for p in p_a])


information_loss = H_X_given_Y - H_X

print(f"Среднее количество информации в принятом ансамбле сообщений относительно переданного: {information_loss} бит")
