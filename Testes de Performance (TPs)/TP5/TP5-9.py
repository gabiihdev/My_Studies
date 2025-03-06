import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
media_horas_trabalhadas = df.groupby('income')['hours-per-week'].mean().round(2)

print(media_horas_trabalhadas)