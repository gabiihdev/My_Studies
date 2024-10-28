""" 3. Escreva um programa que receba dois nomes de usuário e os
    combine de maneira criativa para formar um novo nome """

import random

primeiroNome = input('Digite o primeiro nome:')
segundoNome = input('Digite o segundo nome:')

primeiroNomeDividido = len(primeiroNome) // 2
segundoNomeDividido = len(segundoNome) // 2

novoNome = primeiroNome[:primeiroNomeDividido] + segundoNome[segundoNomeDividido:]

print(f'O nome criativo é {novoNome}.')