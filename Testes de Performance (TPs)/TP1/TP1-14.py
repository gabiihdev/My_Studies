""" 14. Escreva um programa que permita ao usuário votar em três opções
    diferentes e, no final, exiba o número de votos de cada opção. """

votos = {'Honda Civic G10': 0, 'Chevrolet Corvette Z06': 0, 'Nissan Skyline GT-R R34':0}

print('Qual carro você prefere:')
print('1 - Honda Civic G10\n2- Chevrolet Corvette Z06\n3- Nissan Skyline GT-R R34')

while True:
    voto = int(input('Digite o número da sua escolha ou 0 para encerrar a votação:'))

    if voto == 0:
        break
    elif voto == 1:
        votos['Honda Civic G10'] += 1
    elif voto == 2:
        votos['Chevrolet Corvette Z06'] += 1
    elif voto == 3:
        votos['Nissan Skyline GT-R R34'] += 1
    else:
        print('Opção inválida.')

for carro, quantidadeVotos in votos.items():
    print(f'Resultado da votação: {carro} = {quantidadeVotos} votos.')