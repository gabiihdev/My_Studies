import pathlib


def criar_conjunto_nomes_unicos(arq):
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            nomes_unicos = set()
            for linha in arquivo:
                nome = linha.strip().lower()
                nomes_unicos.add(nome)
        return nomes_unicos
    except FileNotFoundError:
        print(">> Arquivo não encontrado.")


DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = DIR_CUR / "nomes.txt"

print(criar_conjunto_nomes_unicos(ARQ))
