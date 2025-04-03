import pandas as pd
from sqlalchemy import create_engine
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DB = f"sqlite:///{DIR_CUR}/imdb.db"

def consultar_dados_BD():
    try:
        engine = create_engine(DB)
        
        df_movies = pd.read_sql("SELECT * FROM movies", con=engine)
        df_movies["title"] = df_movies["title"].str.replace(r"^\d+\.\s*", "", regex=True)

        df_series = pd.read_sql("SELECT * FROM series", con=engine)
        df_series["title"] = df_series["title"].str.replace(r"^\d+\.\s*", "", regex=True)

        return df_movies, df_series

    except Exception as e:
        print(f">> ERRO: consulta ao BD - {e}")  

def exibir_dados_BD(df_movies, df_series):
    print("FILMES\n")
    print(df_movies.to_string(index=False))
        
    print("\nSÉRIES\n")
    print(df_series.to_string(index=False))

if __name__ == "__main__":
    df_movies, df_series = consultar_dados_BD()
    exibir_dados_BD(df_movies, df_series)