import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "Sample-Superstore.csv"
EXCEL = DIR_CUR / "Sample-Superstore.xlsx"

def salvar_e_carregar_excel(CSV, EXCEL):
    df = pd.read_csv(CSV, encoding='ISO-8859-1')

    df.to_excel(EXCEL, index=False)
    print('>> Arquivo Excel salvo com sucesso!!')

    df_carregado = pd.read_excel(EXCEL)
    print('>> Arquivo Excel carregado com sucesso!!')

    return df_carregado

def combinar_excels(EXCEL):
    df = pd.read_excel(EXCEL)
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df_ano_2015 = df[(df['Order Date'].dt.year == 2015)]
    df_ano_2016 = df[(df['Order Date'].dt.year == 2016)]
    df_combinado = pd.concat([df_ano_2015, df_ano_2016])

    print('>> Arquivos Excel dos anos 2015 e 2016 combinados com sucesso!!\n')
    print(df_combinado)

salvar_e_carregar_excel(CSV, EXCEL)
combinar_excels(EXCEL)