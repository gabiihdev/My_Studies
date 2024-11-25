def alternar_letras(string):
    letras_alternadas = []
    for i, letra in enumerate(string):
        if i % 2 == 0:
            letras_alternadas.append(letra.upper())
        else:
            letras_alternadas.append(letra.lower())
            
    return ''.join(letras_alternadas)
    
    
string = 'desenvolvendo habilidades'
print(alternar_letras(string))