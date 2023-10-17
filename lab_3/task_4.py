import math

P_Y = [1/3, 1/3, 1/3]
P_X_given_Y = [2/3, 3/4, 1/2]
H_X_given_Y_total = 0

for i in range(len(P_Y)):
    P_X = P_X_given_Y[i]
    if P_X > 0:
        H_X_given_Y_i = - P_X * math.log2(P_X)
    else:
        H_X_given_Y_i = 0
    H_X_given_Y_total += P_Y[i] * H_X_given_Y_i

print(f"Полная условная энтропия H(X|Y) = {H_X_given_Y_total:.4f} бит")
