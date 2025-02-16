import json
import pathlib


def ler_json(arq):
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            dados_carregados = json.load(arquivo)
        return dados_carregados
    except FileNotFoundError:
        print(">> ERRO: arquivo não encontrado.")


DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = DIR_CUR / "dados.json"

print(ler_json(ARQ))
