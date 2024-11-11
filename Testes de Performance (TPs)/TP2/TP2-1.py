def verificar_maioridade(idades):
    maiores_de_idade = {}
    for nome, idade in idades.items():
        if idade >= 18:
            maiores_de_idade[nome] = idade
    return maiores_de_idade

idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}
print(verificar_maioridade(idades))