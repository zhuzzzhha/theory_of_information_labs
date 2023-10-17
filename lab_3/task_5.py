import math

P_a1 = 1/3
P_a2 = 1/3
P_a3 = 1/3

P_b_given_a = ((0.98, 0.01, 0.01),
               (0.15, 0.75, 0.1),
               (0.3, 0.2, 0.5))

H_X_given_Y = 0

for i in range(3):
    for j in range(3):
        H_X_given_Y -= P_a1 * P_b_given_a[i][j] * math.log2(P_b_given_a[i][j])

print(f"Полная условная энтропия (a) = {H_X_given_Y:.4f} бит")

P_a = [0.7, 0.2, 0.1]

H_B_given_A = 0
for a in range(3):
    for b in range(3):
        if P_b_given_a[a][b] > 0:
            H_B_given_A -= P_a[a] * P_b_given_a[a][b] * math.log2(P_b_given_a[a][b])

print(f"Полная условная энтропия (б) = {H_B_given_A:.4f} бит")
