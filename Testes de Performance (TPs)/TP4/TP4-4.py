def contar_frequencia(string):
    string = string.lower().replace('.', '').replace(',', '')
    palavras = string.split()
    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


string = 'Python é uma linguagem de programação. Python é uma linguagem legal.'
print('Frequência das palavras:', contar_frequencia(string))
