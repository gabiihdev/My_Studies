def verificar_dicionarios(dicionario1, dicionario2):
    for palavra, contagem in dicionario2.items():
        if palavra not in dicionario1 or dicionario1[palavra] != contagem:
            return False
    return True

dicionario1 = {'maçã': 1, 'banana': 2, 'uva': 3, 'goiaba': 4}
dicionario2 = {'maçã': 1, 'banana': 2}

print(verificar_dicionarios(dicionario1, dicionario2))