#БПМ-21-3
#Хлобустова, Жукова, Карякина

# Событие А - купленная продукция будет высшего сорта
# События В1, В2, В3 - соотвестственно продукция 1, 2, 3 предприятий, образуют полную группу
# Задача решается по формуле p(A) = p(B1)*p(A/B1) + p(B2)*p(A/B2) + p(B3)*p(A/B3)

def tem1(pB, pAB):
    pA = 0
    for i in range(len(pB)):
        pA += pB[i]*pAB[i]
    return pA

pB = []
pAB = []
# Вводим проценты
pB = list(map(int, input().split()))
pAB = list(map(int, input().split()))

for i in range(len(pB)):
    pB[i] *= 0.01
    pAB[i] *= 0.01

print(tem1(pB, pAB))
