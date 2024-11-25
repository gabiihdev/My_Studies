def filtrar_palavras(string, indesejadas):
    palavras = string.split()
    palavras_filtradas = []
    for palavra in palavras:
       if palavra.lower() not in indesejadas:
           palavras_filtradas.append(palavra)
    
    return ' '.join(palavras_filtradas)
        
string = 'Eu já estou estudando Python há 3 meses.'
palavras_indesejadas = ['já', '3']

print(filtrar_palavras(string, palavras_indesejadas))