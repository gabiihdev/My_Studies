import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def fazer_consultas_avancadas_sql():
    conn = sqlite3.connect(DB)
    
    consulta1 = '''
    SELECT product_name, SUM(quantity) AS total_vendido
    FROM pedidos
    GROUP BY product_name
    ORDER BY total_vendido DESC
    LIMIT 5
    '''
    
    consulta2 = '''
    SELECT city, SUM(sales) AS total_vendas
    FROM pedidos
    GROUP BY city
    ORDER BY total_vendas DESC
    LIMIT 1
    '''
    
    df_consulta1 = pd.read_sql_query(consulta1, conn)
    df_consulta2 = pd.read_sql_query(consulta2, conn)
    
    print('\nOS 5 PRODUTOS MAIS VENDIDOS:\n')
    print(df_consulta1)
    
    print('\n\nCIDADE COM O MAIOR VOLUME DE VENDAS:\n')
    print(df_consulta2)
    
fazer_consultas_avancadas_sql()