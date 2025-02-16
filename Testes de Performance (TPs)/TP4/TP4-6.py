def somar_dicts(dict1, dict2):
    dicts_somados = dict1.copy()
    
    for chave, valor in dict2.items():
        if chave in dicts_somados:
            dicts_somados[chave] += valor
        else:
            dicts_somados[chave] = valor
            
    return dicts_somados


dict1 = {'Caneta': 6, 'Lápis': 5, 'Borracha': 8, 'Corretivo': 9}
dict2 = {'Borracha': 16, 'Caneta': 12, 'Marca-texto': 10, 'Apontador': 4}
print('Dicionários somados:', somar_dicts(dict1, dict2))