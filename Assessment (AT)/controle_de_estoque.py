def processar_string(estoque_inicial):
    """
    Função:
    Converter a string estoque inicial em uma lista de dicionários.
    
    Return:
    list: lista com dicionários.
    """
    
    produtos = []
    produtos_separados = estoque_inicial.split('#') 

    for produto in produtos_separados:
        info_produto = produto.split(';') 
        produto = {
            "Descrição": info_produto[0],
            "Código": int(info_produto[1]),
            "Qtd_estoque": int(info_produto[2]),
            "Custo_produto": float(info_produto[3]),
            "Preço_venda": float(info_produto[4]),
        }

        produtos.append(produto)
    return produtos


def validar_int(num):
    """
    Função:
    Verificar se o número digitado pelo usuário é inteiro.
    """
    
    while True:
        valor = input(num)
        
        try:
            valor_int = int(valor)
            return valor_int
        
        except ValueError:
            print('>> ERRO: DIGITE UM NÚMERO INTEIRO.\n')


def validar_float(num):
    """
    Função:
    Verificar se o número digitado pelo usuário é float.
    """
    
    while True:
        valor = input(num)
        
        try:
            valor_float = float(valor)
            return valor_float
        
        except ValueError:
            print('>> ERRO: DIGITE UM NÚMERO VÁLIDO.\n')  


def cadastrar_produtos(estoque):
    """
    Função: 
    Cadastrar novos produtos no estoque.
    A função valida a entrada de dados, e caso essa validação seja bem sucedida, o produto é adicionado à lista de estoque.
    """
    
    descricao = input('Digite a descrição do produto: ')
    codigo = validar_int('Digite o código: ')
    for produto in estoque:
        if codigo == produto['Código']:
            print(f'\>> ERRO: EXISTE UM PRODUTO COM O CÓDIGO {codigo} NO ESTOQUE.')
            return
        
    qtd_estoque = validar_int('Digite a quantidade do produto em estoque: ')
    custo_produto = validar_float('Digite o custo do produto: ')
    preco_venda = validar_float('Digite o preço de venda do produto: ')
        
    produto = {
        "Descrição": descricao,
        "Código": codigo,
        "Qtd_estoque": qtd_estoque,
        "Custo_produto": custo_produto,
        "Preço_venda": preco_venda,
    }

    estoque.append(produto)
    print(f'\n>> PRODUTO ({produto["Descrição"].upper()}) CADASTRADO COM SUCESSO!')


def listar_produtos(estoque):
    """
    Função:
    Listar todos os produtos do estoque.
    """
    
    if not estoque:
        print('>> ESTOQUE VAZIO.')
        return
    
    print(f"{'Descrição'.ljust(25)}{'Código'.rjust(17)}{'Quantidade'.rjust(19)}{'Custo do produto'.rjust(24)}{'Preço de venda'.rjust(22)}")
    print('-' * 130)

    for n, produto in enumerate(estoque):
        descricao = produto['Descrição']
        codigo = produto['Código']
        qtd_estoque = produto['Qtd_estoque']
        custo_produto = produto['Custo_produto']
        preco_venda = produto['Preço_venda']
    
        print(descricao.ljust(30), str(codigo).rjust(10), str(qtd_estoque).rjust(15), f"R${custo_produto:,.2f}".rjust(23), f"R${preco_venda:,.2f}".rjust(23))


def ordenar_produtos_por_qtd(estoque):
    """
    Função:
    Ordenar os produtos do estoque de acordo com a quantidade.
    O usuário escolhe se deseja odenar em ordem crescente ou decrescente.
    """
    
    if not estoque:
        print('>> ESTOQUE VAZIO.')
        return
        
    ordem = input('Deseja ordenar os produtos em ordem crescente ou decrescente: ').lower()

    if ordem == 'crescente':
        produtos_ordenados = sorted(estoque, key=lambda x: x['Qtd_estoque'])
        print(f"\n{'PRODUTOS ORDENADOS EM ORDEM CRESCENTE'.rjust(75)}\n")
        print('-' * 130)
        listar_produtos(produtos_ordenados)
        
    elif ordem == 'decrescente':
        produtos_ordenados = sorted(estoque, key=lambda x: x['Qtd_estoque'], reverse=True)
        print(f"\n{'PRODUTOS ORDENADOS EM ORDEM DECRESCENTE'.rjust(75)}\n")
        print('-' * 130)
        listar_produtos(produtos_ordenados)
        
    else:
        print('>> ORDEM INVÁLIDA. ESCOLHA ENTRE "CRESCENTE" OU "DESCRESCENTE".')


def buscar_produto(estoque):
    """
    Função:
    Buscar produtos no estoque por descrição ou código.
    """
    
    if not estoque:
        print('>> ESTOQUE VAZIO.')
        return
    
    item = input('Digite a descrição ou o código do produto que deseja buscar: ')
    produtos_encontrados = []

    try:
        codigo_int = int(item)

        for produto in estoque:
            if codigo_int == produto['Código']:
                produtos_encontrados.append(produto)

    except ValueError:
        for produto in estoque:
            if item.lower() in produto['Descrição'].lower():
                produtos_encontrados.append(produto)
                
    if produtos_encontrados:
        print(f"\n{'PRODUTOS ENCONTRADOS'.rjust(75)}\n")
        print('-' * 130)
        listar_produtos(produtos_encontrados)
    else:
        print('>> PRODUTO NÃO ENCONTRADO.')


def remover_produto(estoque):
    """
    Função:
    Remover produto do estoque com base no código que o usuário digita.
    """
    
    if not estoque:
        print('>> ESTOQUE VAZIO.')
        return
    
    codigo = validar_int('Digite o código do produto: ')
    
    for produto in estoque:
        if codigo == produto['Código']:
            estoque.remove(produto)
            print(f">> PRODUTO COM CÓDIGO {codigo} ({produto['Descrição']}) REMOVIDO COM SUCESSO!")
            return
            
    print('>> PRODUTO NÃO ENCONTRADO.')
            

def consultar_produtos_esgotados(estoque):
    """
    Função:
    Listar todos os produtos que estão esgotados (quantidade em estoque = 0).
    """
    
    if not estoque:
        print('>> ESTOQUE VAZIO')
        return
    
    produtos_esgotados = []
    
    for produto in estoque:
        if produto['Qtd_estoque'] == 0:
            produtos_esgotados.append(produto)
        
    if produtos_esgotados:
        print('PRODUTOS ESGOTADOS:')
        listar_produtos(produtos_esgotados)
    else:
        print('>> NENHUM PRODUTO ESGOTADO.')
        

def fltrar_produtos_com_baixa_qtd(estoque, quantidade_padrao = 5):
    """
    Função:
    Filtrar e listar todos os produtos com baixa quantidade.
    O usuário deve digitar o limite, caso ele deixe em branco, o valor padrão (5) será utilizado. 
    
    Parâmetros:
    estoque (list): lista de produtos no estoque
    quantidade_padrao = quantidade limite a ser considerada caso o usuário não informe uma.
    """
    
    try:
        quantidade_max = input('Digite a quantidade limite dos produtos que deseja filtrar: ')
        
        if quantidade_max:
            quantidade = int(quantidade_max)
        else:
            quantidade = quantidade_padrao
            
        produtos_baixa_qtd = list(filter(lambda produto: produto['Qtd_estoque'] <= quantidade, estoque))
        
        if produtos_baixa_qtd:
            print(f'\nPRODUTOS COM QUANTIDADE MENOR OU IGUAL A {quantidade}:\n')
            print('-' * 130)
            listar_produtos(produtos_baixa_qtd)
        else:
            print(f'NENHUM PRODUTO COM QUANTIDADE MENOR OU IGUAL A {quantidade}.')
        
    except ValueError:
        print('>> ERRO: DIGITE UM NÚMERO INTEIRO.')
        return
        
        
def atualizar_quantidade(estoque):
    """
    Função:
    Atualizar a quantidade de um produto no estoque (entrada ou saída).
    O usuário deve digitar o código do produto que deseja atualizar.
    """
    
    listar_produtos(estoque)
    codigo = validar_int('\nDigite o código do produto: ')
        
    for produto in estoque:
        if codigo == produto['Código']:
            opcao = input('Digite [1] para entrada(aumento) ou [2] para saída(diminuição): ')
                
            if opcao == '1':
                entrada = validar_int('Digite a quantidade de entrada: ')
                produto['Qtd_estoque'] += entrada
                    
                if entrada == 0:
                    print(f"\nNENHUMA ATUALIZAÇÃO FOI FEITA PORQUE A ENTRADA FOI 0.")
                else:
                    print(f"\n>> A QUANTIDADE E ESTOQUE DO PRODUTO ({produto['Descrição']}) FOI ATUALIZADA PARA {produto['Qtd_estoque']}.\n")

            elif opcao == '2':
                saida = validar_int('Digite a quantidade de saída: ')
                 
                if saida == 0:
                    print(f"\n>> NENHUMA ATUALIZAÇÃO FOI FEITA PORQUE A SAÍDA FOI 0.")
                elif saida > produto['Qtd_estoque']:
                    print('\n>> ERRO: A SAÍDA É MAIOR DO QUE A QUANTIDADE EM ESTOQUE.')
                else:
                    produto['Qtd_estoque'] -= saida
                    print(f"\n>> A QUANTIDADE EM ESTOQUE DO PRODUTO ({produto['Descrição']}) FOI ATUALIZADA PARA {produto['Qtd_estoque']}.\n")   

    print('>> PRODUTO NÃO ENCONTRADO.')
        
 
def atualizar_preco(estoque):
    """
    Função:
    Atualizar o preço de venda de um produto no estoque.
    O usuário deve digitar o código do produto que deseja atualizar.
    """
    
    listar_produtos(estoque)
    codigo = validar_int('\nDigite o código do produto: ')
        
    for produto in estoque:
        if codigo == produto['Código']:
            novo_preco = validar_float('Digite o novo preço do produto: ')
            try:
                produto['Preco_venda'] = novo_preco
                print(f"\nPREÇO DO PRODUTO ({produto['Descrição'].upper()}) ATUALIZADO DE R${produto['Preço_venda']:,.2f} PARA R${novo_preco:,.2f}")
                break
                
            except ValueError:
                print('>> ERRO: DIGITE UM NÚMERO VÁLIDO.')
                    
    print('>> PRODUTO NÃO ENCONTRADO.')


def calcular_total_estoque(estoque):
    """
    Função:
    Calcular o valor total do estoque (quantidade do produto * preço de venda)
    """
    
    total = 0

    print(f"\n{'Produto'.ljust(38)} {'Total em estoque'.rjust(10)}")
    print('-' * 60)
    
    for produto in estoque:
        total_produto = produto['Qtd_estoque'] * produto['Preço_venda']
        print(f"{produto['Descrição'].ljust(40)} R${total_produto:,.2f}".rjust(20))
        total += total_produto
    
    print(f'\nTOTAL EM ESTOQUE = R${total:,.2f}')


def calcular_lucro_presumido(estoque):
    """
    Função:
    Calcular o lucro presumido do estoque (preço de venda - custo do produto) * quantidade em estoque
    """
    
    lucro_total = 0 
    print(f"\n{'Produto'.ljust(38)} {'Lucro Presumido'.rjust(10)}")
    print('-' * 60)   
    
    for produto in estoque:
        lucro_produto = (produto['Preço_venda'] - produto['Custo_produto']) * produto['Qtd_estoque']
        print(f"{produto['Descrição'].ljust(40)} R${lucro_produto:,.2f}".rjust(20))
        lucro_total += lucro_produto
        
    print(f'\nLUCRO TOTAL PRESUMIDO DO ESTOQUE = R${lucro_total:,.2f}')
    
  
def gerar_relatorio_geral(estoque):
    """
    Função:
    Gerar um relatório geral do estoque com todas as informações dos produtos e os cálculos.
    """
    
    if not estoque:
        print('>> ESTOQUE VAZIO.')
        return
    
    print(f"\n{'RELÁTORIO GERAL DO ESTOQUE'.rjust(75)}\n")
    print('-' * 130)
    print(f"{'Descrição'.ljust(25)}{'Código'.rjust(17)}{'Quantidade'.rjust(19)}{'Custo do produto'.rjust(24)}{'Preço de venda'.rjust(22)}{'Valor total'.rjust(22)}")
    print('-' * 130)

    custo_total = 0
    faturamento_total = 0

    for produto in estoque:
        descricao = produto['Descrição']
        codigo = produto['Código']
        qtd_estoque = produto['Qtd_estoque']
        custo_produto = produto['Custo_produto']
        preco_venda = produto['Preço_venda']
        total_produto =  qtd_estoque * preco_venda
        custo_total += qtd_estoque * custo_produto
        faturamento_total += total_produto
        
        print(descricao.ljust(30), str(codigo).rjust(10), str(qtd_estoque).rjust(15), f"R${custo_produto:,.2f}".rjust(23), f"R${preco_venda:,.2f}".rjust(23), f"R${total_produto:,.2f}".rjust(23))
    
    print('-' * 130)

    print(f"\n{'CUSTO TOTAL DO ESTOQUE:'.ljust(117)} R${custo_total:,.2f}".rjust(117))
    print(f"{'FATURAMENTO TOTAL DO ESTOQUE:'.ljust(117)} R${faturamento_total:,.2f}".rjust(117))
    
    
def menu():
    while True:
        print('_' * 130)
        print('\n==================== MENU ====================')
        print('[1] - Cadastrar produto')
        print('[2] - Listar produtos')
        print('[3] - Ordenar produtos')
        print('[4] - Buscar produto')
        print('[5] - Remover produto')
        print('[6] - Consultar produtos esgotados')
        print('[7] - Filtrar produtos com baixa quantidade')
        print('[8] - Atualizar quantidade do produto')
        print('[9] - Atualizar preço do produto')
        print('[10] - Calcular valor total do estoque')
        print('[11] - Calcular lucro presumido do estoque')
        print('[12] - Gerar relatório geral do estoque')
        print('[0] - Sair do programa\n')

        opcao = input('ESCOLHA UMA OPÇÃO: ')
        print('_' * 130)
        
        if opcao == '1':
            cadastrar_produtos(estoque)
        elif opcao == '2':
            listar_produtos(estoque)
        elif opcao == '3':
            ordenar_produtos_por_qtd(estoque)
        elif opcao == '4':
            buscar_produto(estoque)
        elif opcao == '5':
            remover_produto(estoque)
        elif opcao == '6':
            consultar_produtos_esgotados(estoque)
        elif opcao == '7':
            fltrar_produtos_com_baixa_qtd(estoque)
        elif opcao == '8':
            atualizar_quantidade(estoque)
        elif opcao == '9':
            atualizar_preco(estoque)
        elif opcao == '10':
            calcular_total_estoque(estoque)
        elif opcao == '11':
            calcular_lucro_presumido(estoque)
        elif opcao == '12':
            gerar_relatorio_geral(estoque)
        elif opcao == '0':
            print('Fim!')
            break
        else:
            print('OPÇÃO INVÁLIDA.')


estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
estoque = processar_string(estoque_inicial)
menu()