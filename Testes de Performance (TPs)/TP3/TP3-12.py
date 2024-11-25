def combinar_listas(lista1, lista2):
    lista1.extend(lista2)
    
    return lista1

lista1 = [1, 2, 3 , 4, 5]
lista2 = [6, 7, 8, 9, 10]
print(combinar_listas(lista1, lista2))