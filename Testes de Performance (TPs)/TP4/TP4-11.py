import csv


def escrever_csv(arq, lista_dicts):
    cabecalhos = lista_dicts[0].keys()

    with open(arq, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalhos)
        escritor.writeheader()
        escritor.writerows(lista_dicts)

    print(f'>> Arquivo "{arq}" criado com sucesso!!')


lista_supemercado = [
    {"Produto": "Arroz", "Preço": 20.50, "Quantidade": 100},
    {"Produto": "Feijão", "Preço": 8.90, "Quantidade": 150},
    {"Produto": "Leite", "Preço": 5.75, "Quantidade": 200},
    {"Produto": "Óleo", "Preço": 7.30, "Quantidade": 120},
    {"Produto": "Açúcar", "Preço": 4.50, "Quantidade": 180}
]

escrever_csv("supermercado.csv", lista_supemercado)
