import random

def escolher_frutas():
    frutas_disponiveis = input('Digite as frutas disponíveis (separadas por vírgula):')
    frutas = [fruta.strip() for fruta in frutas_disponiveis.split(',')]
    
    while True:
        quantidade_das_frutas = input('Digite a quantidade disponível de cada fruta (separadas por vírgula):')
        quantidades = [int(quantidade.strip()) for quantidade in quantidade_das_frutas.split(',')]
        
        if len(quantidades) == len(frutas):
            break
        elif len(quantidades) > len(frutas):
            print('O número de quantidades é maior do que o número de frutas. Será contabilizado somente até o último índice da lista de frutas.')
            quantidades = quantidades[:len(frutas)]
            break
        else:
            print('O número de quantidades é menor do que o número de frutas. Reescreva a lista de quantidades.')
            
    fruta_escolhida = random.choice(frutas)
    index_da_fruta = frutas.index(fruta_escolhida)
    quantidade_fruta = quantidades[index_da_fruta]
    
    print(f'A fruta escolhida para presentear foi {fruta_escolhida} e a quantidade é {quantidade_fruta}.')

escolher_frutas() 