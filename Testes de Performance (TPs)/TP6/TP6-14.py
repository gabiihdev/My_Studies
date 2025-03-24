import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def filtrar_pedidos_com_lucro_positivo():
    conn = sqlite3.connect(DB)
    
    query = """
        SELECT * FROM pedidos
        WHERE profit > 0
        """
        
    pedidos_lucro_positivo = pd.read_sql_query(query, conn)
    pedidos_lucro_positivo.to_csv(DIR_CUR / "pedidos_lucrativos.csv", index=False)

    print('>> Pedidos com lucro positivo salvos com sucesso no arquivo CSV "pedidos_lucrativos.csv"!!')
    conn.close()
    
filtrar_pedidos_com_lucro_positivo()