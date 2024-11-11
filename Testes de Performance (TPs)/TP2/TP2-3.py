def contar_frequencia(numeros):
    frequencia = {}
    for numero in numeros:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
            
    return dict(sorted(frequencia.items()))    

lista = [4, 1, 5, 2, 3, 2, 4, 4]
print(contar_frequencia(lista))