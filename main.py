import csv
from config import URL, URL_BASE
import requests
from bs4 import BeautifulSoup

paginas = []

# Criar arquivo .csv
arquivo_csv = csv.writer(open('nomes_artistas_z.csv', 'w', newline='\n'))
arquivo_csv.writerow(['Nomes_Artistas', 'URL_Artistas'])

# Criando/Abrindo todas as paginas com artistas sobrenome 'z'
for num_page in range(1, 5):
    paginas.append(f"https://web.archive.org/web/20121007172955/httpx://www.nga.gov/collection/anZ{num_page}.htm")

# percorrer a lista paginas para extrar os dados
for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # Remover links inferiores do 'AlphaNav' não desejados.
    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()

    # Pegar dentro da classe 'BodyText' o conteúdo completo especifido do html
    bloco_nomes_artistas = soup.find(class_='BodyText')
    lista_nomes_artistas = bloco_nomes_artistas.find_all('a')

    # For looping para mostra apenas o conteúdo: Nome dos artistas
    for nome_artista in lista_nomes_artistas:
        nomes = nome_artista.contents[0]  # pega conteúdo que está entre '<a></a>' ou seja, dentro dessa tag.
        links = f"{URL_BASE}{nome_artista.get('href')}"  # Assim consigo buscar apenas o link que preciso
        arquivo_csv.writerow([nomes, links])
        print(nomes)
        print(links)

# # fazendo looping usando prittify para listar de forma clara link e seus artistas
# for nome_artista in lista_nomes_artistas:
#     print(nome_artista.prettify())
