import re
import pathlib


def criar_indice_invertido(arq):
    indice_invertido = {}

    with open(arq, 'r', encoding='utf-8') as arquivo:
        for num_linha, linha in enumerate(arquivo, 1):
            palavras = re.findall(r'\b\w+\b', linha.lower())
            for palavra in palavras:
                if palavra not in indice_invertido:
                    indice_invertido[palavra] = set()
                indice_invertido[palavra].add(num_linha)

    return indice_invertido


DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = DIR_CUR / "texto.txt"

indice = criar_indice_invertido(ARQ)
print(indice)
