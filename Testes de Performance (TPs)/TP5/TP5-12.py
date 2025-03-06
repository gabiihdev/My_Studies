import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
mulheres_mais_40h = df[(df['gender'] == 'Female') & (df['hours-per-week'] > 40)]

print(mulheres_mais_40h)