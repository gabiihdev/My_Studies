import pandas as pd

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print('>> Arquivo carregaado com sucesso!!')
            print(arquivo.readlines)
    except FileNotFoundError:
        print('>> ERRO: Arquivo não encontrado.')
        pass
    
carregar_arquivo("nome_arquivo")