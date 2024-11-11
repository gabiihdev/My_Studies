def ordenar_lista(lista):
    for i in range(len(alunos)):
        maior_index = i
        for j in range(i + 1, len(alunos)):
            if list(lista[j].values())[0] > list(lista[maior_index].values())[0]:
                maior_index = j
                
        lista[i], lista[maior_index] = lista[maior_index], lista[i]
        
    return lista

def exibir_lista_ordenada(lista):
    print(f'\nAlunos ordenados por nota em ordem descrescente:')
    for aluno in lista:
        nome = list(aluno.keys())[0]
        nota = list(aluno.values())[0]
        print(f'{nome}: {nota}')
    

alunos = [
    {'Gabriel': 8.0},
    {'Letícia': 5.5},
    {'Lívia': 7.2},
    {'João': 5.0},
    {'Heitor': 9.6},
    {'Matheus': 6.1},
    {'Pérola': 8.7},
]

exibir_lista_ordenada(ordenar_lista(alunos))