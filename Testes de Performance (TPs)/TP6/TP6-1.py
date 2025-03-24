import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "Sample-Superstore.csv"

def ler_csv(CSV):
    df = pd.read_csv(CSV, encoding='ISO-8859-1')
    print('\nEXIBIÇÃO DAS 5 PRIMEIRAS LINHAS:\n')
    print(df.head(5))

def contar_linhas_colunas(CSV):
    df = pd.read_csv(CSV, encoding='ISO-8859-1')
    linhas, colunas = df.shape
    print('\n\nQUANTIDADE DE LINHAS E COLUNAS:\n')
    print(f'>> Existem {linhas} linhas e {colunas} colunas no dataset.')

def verificar_valores_nulos(CSV):
    df = pd.read_csv(CSV, encoding='ISO-8859-1')
    valores_nulos = df.isnull().sum()
    print('\n\nQUANTIDADE DE VALORES NULOS POR COLUNA:\n')
    print(valores_nulos)

ler_csv(CSV)
contar_linhas_colunas(CSV)
verificar_valores_nulos(CSV)