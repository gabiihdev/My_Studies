""" 7. Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça
    feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso). """
from os.path import altsep

peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura (metros) :'))

imc = round(peso / (altura ** 2), 2)

if imc < 18.5:
    print(f'O seu IMC é {imc}\nClassificação: Abaixo do peso (menor que 18.5)')
elif 18.5 <= imc <= 24.99:
    print(f'O seu IMC é {imc}\nClassificação: Peso normal (entre 18.5 e 24.99)')
elif 25 < imc < 30:
    print(f'O seu IMC é {imc}\nClassificação: Sobrepeso (acima de 24.99)')
else:
    print(f'O seu IMC é {imc}\nClassificação: Obesidade (acima de 30)')