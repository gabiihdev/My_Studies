def classificar_alunos(notas):
    classificacao = {'Aprovado': [], 'Reprovado': []}

    for aluno, nota in notas.items():
        if nota >= 7:
            classificacao['Aprovado'].append(aluno)
        else:
            classificacao['Reprovado'].append(aluno)
            
    return classificacao


notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5}
print(classificar_alunos(notas))