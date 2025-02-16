import json


def escrever_dict_json(arq, dict):
    with open(arq, 'w', encoding='utf-8') as arquivo:
        json.dump(dict, arquivo, indent=4)

    print(f'>> Dicionário salvo com sucesso em "{arq}" !!')


dados_aluna = {
    "nome": "Gabriela",
    "idade": 18,
    "cidade": "Rio de Janeiro",
    "curso": "ADS",
    "semestre": 2,
    "habilidades": ["JavaScript", "HTML", "CSS", "Python", "SQL"]
}

escrever_dict_json("aluna.json", dados_aluna)
