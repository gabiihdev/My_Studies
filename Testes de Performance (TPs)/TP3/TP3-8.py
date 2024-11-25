def retornar_elem_unicos(lista):
    elem_unicos = set()
    for listinha in lista:
        elem_unicos.update(listinha)
        
    return list(elem_unicos)

lista = [[2,4,6], [4, 5, 1, 6], [2, 2, 6]]
print(retornar_elem_unicos(lista))