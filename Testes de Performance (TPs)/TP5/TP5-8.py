import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
bachelors = df[df['education'] == 'Bachelors'].shape[0]

print(f'>> {bachelors} pessoas possuem nível de educação "Bachelors" no dataset.')