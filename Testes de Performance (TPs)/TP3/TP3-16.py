def gerenciar_lista_compras(compras):
    while True:
        print(f'\nLista de compras: {compras}\n')
        print('- Digite "fim" para encerrar.')
        print('- Digite "remover" seguido do nome do produto ou seu índice para remover o item da lista.')
        print('- Digite "adicionar" seguido do índice e do nome do produto para adicionar o item na lista na posição indicada.')
        operacao = input('\nOperação que deseja fazer: ').strip()
        
        if operacao == 'fim':
            print('Operação encerrada.')
            break
        
        elif operacao.startswith('remover'):
            comando = operacao.split()
            if len(comando) == 2 and comando[1].isdigit():
                indice = int(comando[1])
                if 0 <= indice < len(compras):
                    item_removido = compras.pop(indice)
                    print(f'Item {item_removido} removido da lista com sucesso.')
                else:
                    print(f'Índice fora do intervalo.')

            else:
                item = comando[1].strip().lower()  
                encontrado = False
                for i, produto in enumerate(compras):
                    if produto.lower() == item:  
                        compras.pop(i)
                        print(f'Item {produto} removido da lista com sucesso.')
                        encontrado = True
                        break
                if not encontrado:
                    print(f'Item {item} não encontrado na lista.')
                
                    
        elif operacao.startswith('adicionar'):
            comando = operacao.split()
            if len(comando) == 3 and comando[1].isdigit():
                indice = int(comando[1])
                item = comando[2]
                if 0 <= indice <= len(compras):
                    compras.insert(indice, item)
                    print(f'Item {item} adicionado à lista com sucesso.')
                else:
                    print(f'Índice {indice} fora do intervalo.')
                    

compras = ['Arroz', 'Feijão', 'Farinha', 'Macarrão', 'Sal', 'Frango', 'Leite', 'Detergente', 'Sabão']
gerenciar_lista_compras(compras)