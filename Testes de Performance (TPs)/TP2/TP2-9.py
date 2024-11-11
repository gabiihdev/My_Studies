def verificar_palindromo(texto):
    texto = texto.replace(' ', '').lower()
    
    if texto == texto[::-1]:
        return 'A string é um palíndromo!'
    else:
        return 'A string não é um palíndromo!'
    
string = 'A mala nada na lama'
print(verificar_palindromo(string))