import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
df['capital_difference'] = df['capital-loss'] - df['capital-gain']

print(df[['capital-loss', 'capital-gain', 'capital_difference']])