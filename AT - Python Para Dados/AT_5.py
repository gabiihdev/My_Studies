from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

URL_FILMES = "https://www.imdb.com/chart/top/"
URL_SERIES = "https://www.imdb.com/pt/chart/toptv/"
HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.google.com/"}

def acessar_url(URL):
    try:
        req = Request(URL, headers=HEADERS)
        html = urlopen(req).read()
        return html
    except Exception as ex:
        print('>> ERRO: acesso a URL')
        exit()

def extrair_titulos_filmes(bs_filmes):
    lista = bs_filmes.find("ul", class_= "ipc-metadata-list") 
    return [titulo.h3.text for titulo in lista]

def exibir_10_primeiros_filmes(titulos):
    print('TOP 10 FILMES DO IMBD\n')
    for titulo in titulos[:10]:
        print(titulo)
       
        
html_filmes = acessar_url(URL_FILMES)
html_series = acessar_url(URL_SERIES)

bs_filmes = BeautifulSoup(html_filmes, "html.parser")
bs_series = BeautifulSoup(html_series, "html.parser")

if __name__ == "__main__":
    titulos = extrair_titulos_filmes(bs_filmes)
    exibir_10_primeiros_filmes(titulos)