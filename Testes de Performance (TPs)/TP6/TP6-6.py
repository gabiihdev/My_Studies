import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def excluir_pedidos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pedidos WHERE sales < 50.00")
    conn.commit()
    
    print('>> Pedidos com valor de venda menor que R$ 50,00 excluídos com sucesso!!')

def adicionar_coluna_status():
    conn =  sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("""
    ALTER TABLE pedidos
    ADD COLUMN status TEXT DEFAULT 'Normal'           
    """)
    
    conn.commit()
    print('>> Coluna "status" adicionada com sucesso na tabela "pedidos"')
    
def atualizar_status():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("""
    UPDATE pedidos
    SET status = 'Pedido em Revisão'
    WHERE quantity > 10
    """)
    
    conn.commit()   
    print('>> Pedidos com quantidade maior que 10 atualizados para "Pedido em Revisão" com sucesso!!\n')
    
    df = pd.read_sql_query("SELECT * FROM pedidos", conn)
    print(df)

    conn.close()

excluir_pedidos()
adicionar_coluna_status()
atualizar_status()