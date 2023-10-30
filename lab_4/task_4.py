import math


P = [[0.99, 0.02, 0, 0],
     [0.01, 0.98, 0.01, 0.01],
     [0, 0, 0.98, 0.02],
     [0, 0, 0.01, 0.97]]

p_x = [0.04, 0.2, 0.2, 0.2]

H_X_given_Y = 0

for b in range(len(P[0])):
    for a in range(len(P)):
        if P[a][b] != 0:
            H_X_given_Y += p_x[b] * P[a][b] * math.log2(1 / P[a][b])

H_X = sum([-p * math.log2(p) for p in p_x])


information_loss = H_X_given_Y - H_X

print(f"Среднее количество информации в принятых сообщениях относительно переданных: {information_loss} бит")
