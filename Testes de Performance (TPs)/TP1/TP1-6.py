""" 6. Escreva um programa onde o usuário deve adivinhar um número secreto. O programa
    deve dizer se o palpite está correto, muito alto ou muito baixo. """

import random

numeroSecreto = random.randint(0,20)
print('O número secreto está entre 0 e 20.')

while True:
    numeroUsuario = int(input('Digite o seu palpite:'))

    if numeroUsuario > numeroSecreto:
        print('O seu palpite está muito alto.')
    elif numeroUsuario < numeroSecreto:
        print('O seu palpite está muito baixo.')
    else:
        print('Parabéns, o seu palpite está correto.')
        break