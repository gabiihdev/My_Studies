import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
df['marital_status_code'] = pd.factorize(df['marital-status'])[0]

print(df[['marital-status', 'marital_status_code']])