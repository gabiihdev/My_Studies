import pandas as pd

def carregar_arquivo(arquivo):
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        print('ERRO: arquivo não encontrado.')
    else:
        print('>> Arquivo carregado com sucesso!!')
        print(df)
        
carregar_arquivo("arquivo.csv")