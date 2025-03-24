import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def fazer_consultas_basicas_sql():
    conn = sqlite3.connect(DB)
    
    consulta1 = '''
    SELECT * FROM pedidos
    WHERE profit > 100
    '''
    
    consulta2 = '''
    SELECT * FROM pedidos
    WHERE segment = 'Consumer'
    '''
    
    df_consulta_1 = pd.read_sql_query(consulta1, conn)
    df_consulta_2 = pd.read_sql_query(consulta2, conn)
    
    print('\nPEDIDOS COM O LUCRO MAIOR QUE R$ 100,00:\n')
    print(df_consulta_1)
    
    print('\n\nPEDIDOS DO SEGMENTO "CONSUMER":\n')
    print(df_consulta_2)

fazer_consultas_basicas_sql() 