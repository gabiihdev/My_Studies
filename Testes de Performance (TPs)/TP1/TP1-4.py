""" 4. Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão)
    e dois números,e então execute a operação escolhida com os números. """

operacao = input('Escolha a operação que deseja realizar (adição, subtração, multiplicação ou divisão): ').lower()
primeiroNumero = int(input('Digite o primeiro número:'))
segundoNumero = int(input('Digite o segundo número:'))

if operacao == 'adição':
    soma = primeiroNumero + segundoNumero
    print(f'Resultado: {primeiroNumero} + {segundoNumero} = {soma}')
elif operacao == 'subtração':
    subtracao = primeiroNumero - segundoNumero
    print(f'Resultado: {primeiroNumero} - {segundoNumero} = {subtracao}')
elif operacao == 'multiplicação':
    multiplicacao = primeiroNumero * segundoNumero
    print(f'Resultado: {primeiroNumero} * {segundoNumero} = {multiplicacao}')
elif operacao == 'divisão':
    divisao = primeiroNumero / segundoNumero
    print(f'Resultado: {primeiroNumero} / {segundoNumero} =  {divisao}')
else:
    print('Operação inválida.')