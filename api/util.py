import requests
import json
from bs4 import BeautifulSoup

from services import criar_clube



def salvarImg(img_url, img_name, serie):    
    image = requests.get(img_url).content
    with open(f'escudos/{serie}/{img_name}', 'wb') as f:
        f.write(image)


link = "https://ge.globo.com/futebol/brasileirao-serie-a/"
req = requests.get(link)
soup = BeautifulSoup(req.content, 'html.parser')

mapeamento_ids = {
    "tab-content-1": "serie_a",
    "tab-content-2": "serie_b",
    "tab-content-3": "internacional",
}

mosaico_equipes = soup.find_all('div', class_='mosaico__equipes')

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
        #salvarImg(img, img_nome, nome_serie)
        criar_clube(nome, nome_serie, img_nome)        
        print(nome, img, nome_serie)
