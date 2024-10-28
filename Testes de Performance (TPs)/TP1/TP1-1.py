""" 1. Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule
    e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números. """

primeiroNumero = int(input('Insira o primeiro número:'))
segundoNumero = int(input('Insira o segundo número:'))

soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero
divisaoInteira = primeiroNumero // segundoNumero

print(f'Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}')
print(f'Divisão: {divisao}\nDivisão Inteira: {divisaoInteira}')
