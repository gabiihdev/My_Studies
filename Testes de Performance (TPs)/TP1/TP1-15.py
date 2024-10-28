""" 15. Crie um programa que apresente ao usuário uma série de escolhas (como em
     uma história) e conduza a diferentes resultados com base nessas escolhas. """

print('Você se encontra em uma encruzilhada. O que você faz?')
print('1 - Segue pela estrada da esquerda\n2 - Segue pela estrada da direita')

primeiraEscolha = input('Digite a sua escolha:')

if primeiraEscolha == '1':
    print('Você encontra um lobo faminto! O que você faz?')
    print('1 - Tenta acalmar o lobo\n2 - Corre')

    segundaEscolha = input('Digite a sua escolha:')

    if segundaEscolha == '1':
        print('O lobo se acalma e se torna seu amigo')
    elif segundaEscolha == '2':
        print('Você conseguiu escapar, mas está sozinho e perdido na floresta')
    else:
        print('Escolha inválida!')

elif primeiraEscolha == '2':
    print('Você encontra um tesouro escondido! O que você faz?')
    print('1 - Abre o tesouro\n2 - Ignora o tesouro e segue em frente.')

    terceiraEscolha = input('Digite a sua escolha:')

    if terceiraEscolha == '1':
        print('Parabéns! Você encontrou ouro! Agora você é rico e pode voltar para casa')
    elif terceiraEscolha == '2':
        print('Você seguiu em frente e encontrou um caminho seguro, mas perdeu a chance de ser rico')
    else:
        print('Escolha inválida!')

else:
    print('Escolha inválida!')
