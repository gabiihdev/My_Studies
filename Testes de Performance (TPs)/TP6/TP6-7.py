import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def criar_coluna_total_com_desconto():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT * FROM pedidos", conn)
    
    df['Total com desconto'] = df['sales'] - (df['sales'] * df['discount'])
    df.to_sql('pedidos', conn, if_exists='replace', index=False)
    
    conn.close()
    print('>> Coluna "Total com desconto" criada com sucesso!!')
    
def preencher_valores_nulos():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT * FROM pedidos", conn)
    
    df = df.apply(lambda col: col.fillna("Não Informado") if col.dtype == "object" else col.fillna(0))

    conn.close()
    print('>> Valores nulos preenchidos com sucesso!!')    

def ordenar_df_venda():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT * FROM pedidos", conn)   
    
    df_ordenado = df.sort_values(by='sales', ascending=False)

    conn.close()
    print('>> Dataframe ordenado pelo valor de venda com sucesso!!\n')
    print(df_ordenado)
    
criar_coluna_total_com_desconto()
preencher_valores_nulos()
ordenar_df_venda()