def gerenciar_compras(compras):
    if compras == []:
        print('Não há mais itens para remover.')
    else:
        compras.pop()
        print(f'Lista de compras atualizada: {compras}')

compras = ['Arroz', 'Feijão', 'Farinha', 'Macarrão', 'Sal', 'Frango', 'Leite', 'Detergente', 'Sabão']
gerenciar_compras(compras)