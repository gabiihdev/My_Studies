from AT_5 import bs_filmes

def extrair_dados_filmes(bs_filmes):
    filmes = []
    lista_filmes = bs_filmes.find("ul", class_="ipc-metadata-list")
    
    for filme in lista_filmes.find_all("li", class_="ipc-metadata-list-summary-item"):
        titulo = filme.find("h3", class_="ipc-title__text").text.strip()
        ano = filme.find("span", class_="cli-title-metadata-item").text.strip()
        nota = filme.find("span", class_="ipc-rating-star--rating").text.strip()
        filmes.append((titulo, ano, nota))
        
    return filmes

def exibir_5_primeiros_filmes(filmes):
    print('TOP 5 FILMES DO IMDB\n')
    for titulo, ano, nota in filmes[:5]:
        print(f"{titulo} ({ano}) - Nota: {nota}")

if __name__ == "__main__":
    filmes = extrair_dados_filmes(bs_filmes)
    exibir_5_primeiros_filmes(filmes)