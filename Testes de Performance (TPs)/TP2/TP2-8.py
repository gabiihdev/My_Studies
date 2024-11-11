import random

def adivinhar_numero_magico():
    numero_magico = random.randint(1, 20)
    tentativas = 4
    
    print('Tente adivinhar o número mágico que está entre 1 e 20!')
    
    while tentativas > 0:
        try:
            palpite = int(input('Digite o seu palpite:'))
            
            if palpite < numero_magico:
                print('O seu palpite está abaixo do número mágico.')
            elif palpite > numero_magico:
                print('O seu palpite está acima do número mágico.')
            else:
                print('Parabéns!! Você acertou o número mágico.')
                break
            
            tentativas -= 1
        
        except ValueError:
            print('Insira um número válido.')
            
    if tentativas == 0:
        print(f'Você errou!! O número mágico era {numero_magico}.')
        
adivinhar_numero_magico() 