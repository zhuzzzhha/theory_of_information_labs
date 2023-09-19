# Жукова, Карякина, Хлобустова 
# БПМ-21-3


# формула полной вероятности

def total_probability(*args):

    result = 0
    
    # Вычисляем произведения вероятностей событий и складываем их

    for prob1, prob2 in args:
        result += prob1 * prob2
    
    return result

# формула Байеса 

def bayes_formula(p_a, p_b_given_a, *args):
    p_b = total_probability(*args)

    # (произведение вероятностей)/(полная вероятность)

    p_a_given_b = round((p_a * p_b_given_a) / p_b, 3)
    
    print(f'вероятность того, что посылается сигнал «1» при условии, что принимается сигнал «1»: {p_a_given_b}')
