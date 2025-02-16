def encontrar_elem_unicos(numeros):
    return list(set(numeros))
    
numeros = [10, 9, 10, 8, 7, 6, 5, 5, 5, 4, 2, 1, 2, 3]
print('Lista de elementos únicos:', encontrar_elem_unicos(numeros))