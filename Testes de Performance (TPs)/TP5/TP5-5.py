import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
linhas, colunas = df.shape

print(f'>> Existem {linhas} linhas e {colunas} colunas no dataset.')