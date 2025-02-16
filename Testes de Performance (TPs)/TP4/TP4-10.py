import csv
import pathlib


def ler_csv(arq):
    try:
        with open(arq, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print('>> ERRO: arquivo não encontrado.')


DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = DIR_CUR / "funcionarios.csv"

ler_csv(ARQ)
