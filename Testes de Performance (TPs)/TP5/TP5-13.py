import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
salarios_e_idades_ordenados = df.sort_values(by=['income', 'age'], ascending=[False, False])

print(salarios_e_idades_ordenados)