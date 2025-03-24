import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def agrupar_pedidos_por_cidade():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    agrupamento = """
    SELECT city, AVG(sales) AS media_vendas
    FROM pedidos
    GROUP BY city
    """
    
    df = pd.read_sql_query(agrupamento, conn)
    
    print('\nPEDIDOS AGRUPADOS POR CIDADE E CÁLCULO DA MÉDIA DE VENDAS:\n')
    print(df)
    
    conn.close
    
agrupar_pedidos_por_cidade()