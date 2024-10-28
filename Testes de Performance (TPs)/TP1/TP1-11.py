""" 11. Faça um programa que simule o lançamento de um dado. O usuário deve
    escolher quantos dados jogar e o programa deve exibir os resultados. """

import random

quantidadeDeDados = int(input('Quantos dados você deseja jogar?'))
resultados = []

for i in range(quantidadeDeDados):
    resultado = random.randint(1, 6)
    resultados.append(resultado)

print(f'Resultados dos dados: {resultados}')