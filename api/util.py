import re

import requests
import json
from bs4 import BeautifulSoup
import unicodedata
from services.clubeService import criar_clube



def salvarImg(img_url, img_name, serie):    
    image = requests.get(img_url).content
    with open(f'escudos/{serie}/{img_name}', 'wb') as f:
        f.write(image)

link_estadio = 'https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/stadien/wettbewerb/BRA1'
link = "https://ge.globo.com/futebol/brasileirao-serie-a/"
req = requests.get(link)
req_estadio = requests.get(link_estadio)
soup = BeautifulSoup(req.content, 'html.parser')
soup_estadio = BeautifulSoup(req_estadio.content, 'html.parser')

mapeamento_ids = {
    "tab-content-1": "serie_a",
    "tab-content-2": "serie_b",
    "tab-content-3": "internacional",
}




mosaico_equipes = soup.find_all('div', class_='mosaico__equipes')
try:
    estadios_equipes = soup_estadio.find_all('td', class_='hauptlink')
except AttributeError:
    print('Nao tem estadio')

for estadio in estadios_equipes:
    Nome_estadio = soup_estadio.find('a').text
    print(estadio)



ids = []

for i in mosaico_equipes:
    id_serie = i.get('id')
    ids.append(id_serie)

for id_pai in ids:
    pesquisa = soup.find('div', id=id_pai)
    nome_serie = mapeamento_ids.get(id_pai,id_pai)
    
    if pesquisa :
        equipes = pesquisa.find_all('div', class_='mosaico__equipes-items')

    for equipe in equipes:        
        img = equipe.find('img')['data-src']
        nome = equipe.find('a')['data-slug-equipe-sde']
        img_nome = f'{nome}.svg'
        #estadio = equipe.find('span', class_='mosaico__equipes-items-estadio').text
        #salvarImg(img, img_nome, nome_serie)
        #criar_clube(nome, nome_serie, img_nome)        
        #print(nome, img, nome_serie)

def remover_acentos(texto) -> str:
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.lstrip()
    texto = texto.rstrip()
    texto = texto.lower()
    texto = texto.replace(' ', '-')
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


print(remover_acentos('São Paulo .'))