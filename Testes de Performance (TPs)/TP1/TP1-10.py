""" 10. Escreva um programa que combine elementos aleatórios de listas diferentes
    (personagens, ações, locais) para criar uma história curiosa. """

personagens = ['O Thor', 'A Mulher Maravilha', 'O Capitão América', 'O Mutano', 'A Estelar', 'A Kitana']
acoes = ['lutou contra o Thanos', 'salvou muitas pessoas', 'malha todos os dias', 'se transformou em um cachorro',
         'fez amizade com um alienígena', 'venceu todas as lutas']
locais = ['na guerra', 'na Alemanha', 'em Nova York', 'na rua', 'no espaço sideral', 'na floresta']

import random

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

print(f'História: {personagem} {acao} {local}.')