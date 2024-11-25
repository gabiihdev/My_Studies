def manipular_string(string):
    print(f'String original: {string}')
    
    while True:
        try:
            inicio = int(input('Digite o índice de início: '))
            fim = int(input('Digite o índice de fim: '))
        
            substring = string[inicio:fim]
            print(f'Substring de {inicio} a {fim}: {substring}')
            break
        
        except ValueError:
            print('ERRO: insira um número.')
        except IndexError:
            print('ERRO: os índices estão fora do intervalo.')
        
string = 'Python é incrível!'
manipular_string(string)