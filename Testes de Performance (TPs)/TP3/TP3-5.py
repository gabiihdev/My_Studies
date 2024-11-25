def verificar_maioridade(idades):
    maiores_de_idade = {}
    for nome, idade in idades.items():
        if idade >= 18:
            maiores_de_idade[nome] = idade
            
    return maiores_de_idade

idades = {'Gabriela': 18, 'Matheus': 14, 'Vanessa': 33, 'Gabriel': 13}
print(verificar_maioridade(idades))