import requests
from bs4 import BeautifulSoup
from AT_5 import bs_series
from AT_6 import extrair_dados_filmes, bs_filmes
from AT_7 import *

HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.google.com/"}

filmes_extraidos = extrair_dados_filmes(bs_filmes)
filmes = [Movie(titulo, ano, nota) for titulo, ano, nota in filmes_extraidos]


def obter_total_temporadas(url_serie):
    try:
        resposta = requests.get(url_serie, headers=HEADERS)
        resposta.raise_for_status() 
        soup = BeautifulSoup(resposta.text, 'html.parser')

        seletor_temporadas = soup.find("select", id="browse-episodes-season")
        
        if seletor_temporadas and seletor_temporadas.has_attr("aria-label"):
            temporadas_texto = seletor_temporadas["aria-label"]  
            temporadas = int(temporadas_texto.split()[0]) 
        else:
            temporadas = 1
    
    except requests.exceptions.RequestException as e:
        print(f">> ERRO: acessar a URL- {e}")
    
    return temporadas

def extrair_dados_series(bs_series):
    series = []
    lista_series = bs_series.find("ul", class_="ipc-metadata-list")

    for serie in lista_series.find_all("li", class_="ipc-metadata-list-summary-item"):  
        titulo = serie.find("h3", class_="ipc-title__text").text.strip()
        
        spans = serie.find_all("span", class_="sc-2bbfc9e9-7 jttFlJ cli-title-metadata-item")
        ano = spans[0].text.strip()
        episodios = int(spans[1].text.split()[0])
        
        link = serie.find("a", href=True)["href"]
        url_serie = f"https://www.imdb.com{link}"
        temporadas = obter_total_temporadas(url_serie)
        
        series.append((titulo, ano, temporadas, episodios))
    
    return series

series_extraidas = extrair_dados_series(bs_series)
series = [Series(titulo, ano, temporadas, episodios) for titulo, ano, temporadas, episodios in series_extraidas]

series.append(Series("26. Grey's Anatomy", 2005, 21, 435))
series.append(Series("27. Supernatural", 2005, 15, 327))

def exibir_objetos():
    print('FILMES\n')
    for filme in filmes:
        print(filme)

    print('\nSÉRIES\n')
    for serie in series:
        print(serie)
        
if __name__ == "__main__":
    exibir_objetos()