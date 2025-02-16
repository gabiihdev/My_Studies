def ordenar_tuplas(idades):
    return sorted(idades, key=lambda x: x[1])


lista_tuplas = [('Vanessa', 32), ('Matheus', 15), ('Gabriela', 18), ('Rodrigo', 41), ('Gabriel', 13)]
print('Lista com as idades ordenadas:', ordenar_tuplas(lista_tuplas))
