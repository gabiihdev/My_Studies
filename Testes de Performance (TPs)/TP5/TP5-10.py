import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
cargo_pessoas_mais_50k = df[df['income'] == '>50K']['occupation'].value_counts().head(3)

print(cargo_pessoas_mais_50k)