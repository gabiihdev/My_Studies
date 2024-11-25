def remover_duplicatas(lista):
    palavras_unicas = []
    for palavra in lista:
        if palavra not in palavras_unicas:
            palavras_unicas.append(palavra)
    
    return palavras_unicas
    
lista = ['Maçã', 'Banana', 'Banana', 'Uva', 'Maçã', 'Abacate', 'Manga']
print(remover_duplicatas(lista))