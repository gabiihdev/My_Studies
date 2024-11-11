def registrar_notas_de_alunos():
    
    notas = {}

    while True:
        aluno = input("Digite o nome do aluno ou 'fim' para terminar:")
        if aluno.lower() == 'fim':
            break
    
        try:
            nota = float(input('Digite a nota do aluno:'))
            notas[aluno] = nota
        except ValueError:
            print('Insira uma nota válida.')

    return notas

def exibir_notas(notas):
    print('\nNotas registradas:')
    for aluno, nota in notas.items():
        print(f'{aluno}: {nota}')
        
exibir_notas(registrar_notas_de_alunos())