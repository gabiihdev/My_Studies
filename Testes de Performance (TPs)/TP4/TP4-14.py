import csv
import pathlib


def processar_csv(arq):
    dict = {}

    try:
        with open(arq, 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                nome = linha.get("Nome")
                cidade = linha.get("Cidade")
                if nome and cidade:
                    dict[nome] = cidade
        return dict
    except FileNotFoundError:
        print(f">> ERRO: Arquivo não encontrado.")


DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = DIR_CUR / "nomes_cidades.csv"

print(processar_csv(ARQ))
