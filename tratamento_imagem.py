import requests
import json
from bs4 import BeautifulSoup


def salvarImg(img_url, img_name):
    image = requests.get(img_url).content
    with open(f'escudos/serieA/{img_name}', 'wb') as f:
        f.write(image)


link = "https://ge.globo.com/futebol/brasileirao-serie-a/"
req = requests.get(link)
soup = BeautifulSoup(req.content, 'html.parser')

pesquisa = soup.find_all('div', class_='mosaico__equipes-items')



"""
for i in pesquisa:
    img = i.find('img')['data-src']
    nome = i.find('a')['data-slug-equipe-sde']
    img_nome = f'{nome}.svg'
    salvarImg(img, img_nome)
    print(nome, img)
"""

