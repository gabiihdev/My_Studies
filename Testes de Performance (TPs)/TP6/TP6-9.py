import pandas as pd

def carregar_csv(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv)
        print('>> Arquivo carregado com sucesso!!')
        print(df)
    except FileNotFoundError:
        print('>> ERRO: arquivo não encontrado.')
    except Exception as e:
        print(f'>> ERRO: {e}')
        
carregar_csv("inexistente.csv")