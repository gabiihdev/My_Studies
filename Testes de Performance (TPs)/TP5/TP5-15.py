import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
df['age_decade'] = (df['age'] // 10 * 10).astype(str) + 's'

print(df[['age', 'age_decade']])