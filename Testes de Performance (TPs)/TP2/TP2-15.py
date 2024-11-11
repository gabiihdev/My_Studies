def imprimir_mensagem(nome, idade, cidade='Desconhecida'):
    if cidade == 'Desconhecida':
        print(f'{nome} tem {idade} anos e a cidade é {cidade}.')
    else:
        print(f'{nome} tem {idade} anos e mora em {cidade}.')

imprimir_mensagem('Maria', 30, 'São Paulo')
imprimir_mensagem('João', 28)