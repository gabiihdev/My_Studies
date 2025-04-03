import pandas as pd 
import pathlib
from AT_10 import consultar_dados_BD
df_movies, df_series = consultar_dados_BD()

DIR_CUR = pathlib.Path(__file__).parent.resolve()
DADOS = DIR_CUR / "dados"

def exportar_dados():
    try:
        df_movies.to_csv(DADOS / "movies.csv", index=False)
        df_series.to_csv(DADOS / "series.csv", index=False)

        df_movies.to_json(DADOS / "movies.json", orient="records", indent=4, force_ascii=False)
        df_series.to_json(DADOS / "series.json", orient="records", indent=4, force_ascii=False)

        print(">> Dados exportados com sucesso!!")
    except Exception as e:
        print(f">> ERRO: {e}")

if __name__ == "__main__":
    exportar_dados()
