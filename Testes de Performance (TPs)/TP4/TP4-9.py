def subconjunto_ou_nao(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

conjunto1 = {2, 4, 6, 8, 10}
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('O conjunto 1 é subconjunto do conjunto 2 ?', subconjunto_ou_nao(conjunto1, conjunto2))