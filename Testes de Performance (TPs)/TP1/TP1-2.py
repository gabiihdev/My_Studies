""" 2. Faça um programa que converta um número fornecido de minutos em horas e minutos,
    e depois faça o inverso, convertendo horas e minutos de volta para minutos totais. """

# Minutos convertidos em horas e minutos

minutos = int(input('Insira os minutos:'))

horas = minutos // 60
restoMinutos = minutos % 60

print(f'{minutos} minutos é igual a {horas} horas e {restoMinutos} minutos.')

# Horas e minutos convertidos em minutos

horass = int(input('Insira as horas:'))
minutoss = int(input('Insira os minutos:'))

minutosTotais = (horass * 60) + minutoss

print(f'{horass} horas e {minutoss} minutos é igual a {minutosTotais} minutos.')
