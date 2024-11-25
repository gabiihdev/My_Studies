def filtrar_palavras(lista, n):
    palavras_menores_e_iguais = []
    palavras_maiores = []
    
    for palavra in lista:
        if len(palavra) <= n:
            palavras_menores_e_iguais.append(palavra)
        else:
            palavras_maiores.append(palavra)
            
    return f'Menores ou iguais: {palavras_menores_e_iguais} | Maiores: {palavras_maiores}'

lista = ['Maçã', 'Banana', 'Uva', 'Abacaxi', 'Goiaba', 'Pera', 'Abacate', 'Mamão']
n = 5
print(filtrar_palavras(lista, n))