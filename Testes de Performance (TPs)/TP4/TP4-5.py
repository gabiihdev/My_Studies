def inverter_dict(dict):
    dict_invertido = {}

    for chave, valor in dict.items():
        dict_invertido[valor] = chave

    return dict_invertido


dict = {'Caneta': 'Pen', 'Lápis': 'Pencil', 'Borracha': 'Eraser', 'Apontador': 'Sharpener'}
print('Dicionário invertido:', inverter_dict(dict))
