import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "Sample-Superstore.csv"
DB = DIR_CUR / "superstore.db"

def criar_banco():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        row_id INTEGER PRIMARY KEY,
        order_id TEXT,
        order_date TEXT,
        ship_date TEXT,
        ship_mode TEXT,
        customer_id TEXT,
        customer_name TEXT,
        segment TEXT,
        country TEXT,
        city TEXT,
        state TEXT,
        postal_code TEXT,
        region TEXT,
        product_id TEXT,
        category TEXT,
        sub_category TEXT,
        product_name TEXT,
        sales REAL,
        quantity INTEGER,
        discount REAL,
        profit REAL
    );
    ''')
    
    conn.commit()
    conn.close()
    print('>> Banco de dados criado com sucesso!!')
   
def inserir_dados_df():
    df = pd.read_csv(CSV, encoding='ISO-8859-1')
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    conn = sqlite3.connect(DB)
    df.to_sql('pedidos', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    print('>> Dados do Dataframe inseridos na tabela SQL com sucesso!!')
        
def carregar_dados_df():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT * FROM pedidos", conn)
       
    conn.close()
    print('>> Dados do banco SQL carregados com sucesso para um Dataframe Pandas!!\n')

criar_banco()
inserir_dados_df()
carregar_dados_df()