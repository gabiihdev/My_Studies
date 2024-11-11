def encontrar_soma_prox_de_0(lista):
    soma_mais_proxima = float('inf')
    nums_da_soma = None
    for i in range(len(lista) - 1):
        soma = lista[i] + lista[i + 1]
        
        if abs(soma) < abs(soma_mais_proxima):
            soma_mais_proxima = soma
            nums_da_soma = (lista[i], lista[i + 1])
            
    return nums_da_soma, soma_mais_proxima

lista = [2, 5, 8, 4, 9, 10, 3, 1, 8, 4, 7]
nums, resultado = encontrar_soma_prox_de_0(lista)
print(f'Soma mais próxima de zero: {nums[0]} + {nums[1]} = {resultado}')