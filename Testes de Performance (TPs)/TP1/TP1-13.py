""" 13. Desenvolva um programa que verifique se uma palavra ou frase inserida
    pelo usuário é um palíndromo (lê-se igual de trás para frente). """

palavraOuFrase = input('Digite a palavra ou a frase:').lower()

if palavraOuFrase == palavraOuFrase[::-1]:
    print('É um palíndromo.')
else:
    print(f'Não é um palíndromo.')
    print(f'Observe: {palavraOuFrase} {palavraOuFrase[::-1]}')

# Exemplos: Osso, Ana, radar, Renner, Roma é amor, orava o avaro