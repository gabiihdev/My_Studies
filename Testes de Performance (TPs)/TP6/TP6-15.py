import sqlite3
import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = DIR_CUR / "superstore.db"

def resumir_vendas():
    try:
        conn = sqlite3.connect(DB)
        
        query = """
        SELECT city, SUM(sales) as total_vendas
        FROM pedidos
        WHERE profit > 0
        GROUP BY city
        ORDER BY total_vendas DESC
        """
        
        try:
            resumo_das_vendas = pd.read_sql_query(query, conn)
        except Exception as e:
            print(f'>> Erro ao executar a consulta no banco de dados: {e}')
            return
        
        try:
            resumo_das_vendas.to_csv(DIR_CUR / "resumo_vendas.csv", index=False)
            print('\n>> Resumo das vendas salvo no arquivo CSV "resumo_vendas.csv" com sucesso!!')
        except Exception as e:
            print(f'>> Erro ao salvar o arquivo CSV: {e}')
            return

        print('\nRESUMO DAS VENDAS:\n')
        print(resumo_das_vendas)
        
    except sqlite3.Error as e:
        print(f'>> Erro ao conectar com o banco de dados: {e}')
        
    finally:
        if 'conn' in locals():
            conn.close()

resumir_vendas()