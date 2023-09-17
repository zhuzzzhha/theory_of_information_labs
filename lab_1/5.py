def fact(n):
  if n == 0:
    return 1
  else:
    return n*fact(n-1)

def combinations(n,k):
  return fact(n)/(fact(k)*fact(n-k))


def probability(p, n,k):
  #p - вероятность ошибочной передачи одного бита
  #n - количество битов в последовательности
  #k - количество ошибок в последовательности
  p_0 = (1-p)**n
  p_n = combinations(n,k)*p**k*(1-p)**(n-k)
  print(f"{p_0} - вероятность безошибочной передачи, {p_n} - вероятность передачи последовательности с {k} ошибками")
