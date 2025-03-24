import pandas as pd

def carregar_arquivo(arquivo):
    try:
        df = pd.read_csv(arquivo)
        print('>> Arquivo carregado com sucesso!!')
        print(df)
    except FileNotFoundError:
        print('>> ERRO: arquivo não encontrado, verifique o nome do arquivo.')

carregar_arquivo("dados_inexistentes.csv")