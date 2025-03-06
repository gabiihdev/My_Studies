import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
colunas_com_ausentes = (df.isnull().sum() / len(df) * 100)[lambda x: x > 0]

print(colunas_com_ausentes)