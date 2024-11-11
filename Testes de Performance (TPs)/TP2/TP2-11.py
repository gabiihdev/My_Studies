def acessar_elemento_da_lista(lista):
    
    while True:
        try:
            indice = int(input('Digite o índice que deseja acessar na lista:'))
        
            if indice < 0 or indice >= len(lista):
                print('O índice inserido está fora do intervalo da lista.')
            else:
                print(f'O elemento no índice {indice} é: {lista[indice]}')
                break
        
        except ValueError:
            print('Insira um número válido.')

lista = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'PHP']
acessar_elemento_da_lista(lista)