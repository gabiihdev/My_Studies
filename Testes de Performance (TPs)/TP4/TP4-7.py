def operar_conjuntos(conjunto1, conjunto2):
    operacoes = {
        'União': conjunto1 | conjunto2,
        'Interseção': conjunto1 & conjunto2,
        'Diferença': conjunto1 - conjunto2
    }

    return operacoes

conjunto1 = {2, 4, 5, 6, 8, 10}
conjunto2 = {1, 3, 5, 7, 9, 10}
print('Resultados das operações entre os 2 conjuntos:\n', operar_conjuntos(conjunto1, conjunto2))
