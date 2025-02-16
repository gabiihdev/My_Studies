def remover_elem_duplicados(lista):
    lista_sem_duplicatas = []
    elem_visualizados = set()

    for elem in lista:
        if elem not in elem_visualizados:
            lista_sem_duplicatas.append(elem)
            elem_visualizados.add(elem)

    return lista_sem_duplicatas


frutas = ['Maçã', 'Uva', 'Banana', 'Abacaxi','Goiaba', 'Maçã', 'Uva', 'Banana']
print('Lista sem duplicatas e mantendo a ordem:', remover_elem_duplicados(frutas))
