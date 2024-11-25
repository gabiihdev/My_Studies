def adicionar_palavra(lista, nova_palavra):
    if len(lista) < 3:
        lista.append(nova_palavra)
    else:
        while True:
            try:
                indice = int(input('Digite a posição que deseja inserir a nova palavra na lista: '))
                if 0 <= indice <= len(lista):
                    lista.insert(indice, nova_palavra)
                    break
                else:
                    print('ERRO: posição fora do intervalo da lista.')
            except ValueError:
                print('ERRO: insira um número.')
                
    return lista
                
lista = ['Maçã', 'Banana', 'Uva', 'Abacaxi', 'Goiaba', 'Pera', 'Abacate', 'Mamão']
nova_palavra = 'Manga'
print(adicionar_palavra(lista, nova_palavra))