import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"
EXCEL = DIR_CUR / "relatorio_vendas.xlsx"

def criar_relatorio_de_vendas():
    conn = sqlite3.connect(DB)
    
    query = """
    SELECT *
    FROM pedidos
    """
    
    df = pd.read_sql_query(query, conn)
        
    df_agrupado = df.groupby("category").agg(
        total_vendas=pd.NamedAgg(column="sales", aggfunc="sum"),
            total_lucro=pd.NamedAgg(column="profit", aggfunc="sum")
        ).reset_index()

    with pd.ExcelWriter(EXCEL, engine='xlsxwriter') as writer:
        for categoria in df["category"].unique():
            df_categoria = df[df["category"] == categoria]
            df_categoria.to_excel(writer, sheet_name=categoria, index=False)
            
        df_agrupado.to_excel(writer, sheet_name="Resumo Geral", index=False)
        
        print('>> Relatório de vendas gerado e exportado para "relatorio_vendas.xlsx" com sucesso!!')
        conn.close()
        
criar_relatorio_de_vendas()