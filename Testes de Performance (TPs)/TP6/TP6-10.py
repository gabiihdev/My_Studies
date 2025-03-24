import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def verificar_valores_negativos_e_corrigir():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE quantity < 0")
    valores_negativos = cursor.fetchone()[0]
    
    if valores_negativos > 0:
        print(f'>> Existem {valores_negativos} pedidos com valores negativos na coluna "quantidade"')
    
        cursor.execute("UPDATE pedidos SET quantity = 0 WHERE quantity < 0")
        conn.commit()
        
        print('>> Valores negativos atualizados para 0.')
    else:
        print('>> Não existem valores negativos na coluna "quantidade".')
        
    conn.close()
        
verificar_valores_negativos_e_corrigir()