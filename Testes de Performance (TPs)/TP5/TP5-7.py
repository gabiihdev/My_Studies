import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
num_categorias_workclass = df["workclass"].nunique()
categorias_workclass = df["workclass"].unique()

print(f'>> Existem {num_categorias_workclass} categorias diferentes na coluna "workclass".')
print(f'>> As categorias são: {categorias_workclass}')