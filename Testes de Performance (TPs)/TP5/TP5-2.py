'''

2 - Quais tipos de dados o Pandas aceita e como ele os armazena internamente? Justifique sua resposta com exemplos concretos.

Resposta: O Pandas aceita vários tipos de dados e os armazena de forma otimizada, geralmente usando NumPy.

'''

import pandas as pd

df = pd.DataFrame({
    'nomes': ['Gabriela', 'Rodrigo', 'Vanessa'],
    'idades': [18, 42, 33],
    'aniversários': pd.to_datetime(['2006-03-28', '1983-02-17', '1991-04-23']),
    'notas': [9.0, 8.0, 7.0]
})

print(df.dtypes)