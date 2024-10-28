""" 9. Desenvolva um programa que aplique descontos progressivos com base no valor da compra:
    desconto de 10% para compras acima de R$100, 15% para compras acima de R$200,seguindo a
    projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%. """

valorCompra = float(input('Digite o valor da compra: R$'))

if valorCompra <= 100:
    print('Não há desconto.')
elif 100 < valorCompra <= 200:
    desconto = valorCompra * 0.10
    valorAtualizado = valorCompra - desconto
    print(f'Você ganhou 10% de desconto. Valor da compra atualizado: R${valorAtualizado:.2f}')
elif 200 < valorCompra <= 300:
    desconto = valorCompra * 0.15
    valorAtualizado = valorCompra - desconto
    print(f'Você ganhou 15% de desconto. Valor da compra atualizado: R${valorAtualizado:.2f}')
elif 300 < valorCompra <= 400:
    desconto = valorCompra * 0.20
    valorAtualizado = valorCompra - desconto
    print(f'Você ganhou 20% de desconto. Valor da compra atualizado: R${valorAtualizado:.2f}')
else:
    desconto = valorCompra * 0.25
    valorAtualizado = valorCompra - desconto
    print(f'Você ganhou 25% de desconto. Valor da compra atualizado: R${valorAtualizado:.2f}')
