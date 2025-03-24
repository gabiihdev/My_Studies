import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def resumir_vendas():
    conn = sqlite3.connect(DB)
    
    query = """
    SELECT city, SUM(sales) as total_vendas
    FROM pedidos
    WHERE profit > 0
    GROUP BY city
    ORDER BY total_vendas DESC
    """
    
    resumo_das_vendas = pd.read_sql_query(query, conn)
    resumo_das_vendas.to_csv(DIR_CUR / "resumo_vendas.csv")
    print('\n>> Resumo das vendas salvo no arquivo CSV "resumo_vendas.csv" com sucesso!!')
    print('\nRESUMO DAS VENDAS:\n')
    print(resumo_das_vendas)

resumir_vendas()