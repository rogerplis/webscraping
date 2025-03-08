from collections import defaultdict
import json
from pathlib import Path
from sqlalchemy.future import select

from api.config import session
from api.model import Clubes
from api.schemas.clubeSchema import ClubesSchemaUpdate

file_path = Path(__file__).parent.parent / "dados" / "dados.json"



"""Area de Clubes"""
def criar_clube(nome: str, serie: str, escudo: str, estadio: str, cidade: str, sigla: str):
    clube = Clubes(nome=nome, serie=serie, escudo=escudo, estadio=estadio, cidade=cidade, sigla=sigla)
    session.add(clube)
    session.commit()
    return clube


def get_all_clubes():
    stmt = select(Clubes)    
    stmt = stmt.order_by(Clubes.serie)
    clubes = session.execute(stmt).scalars().all()
    agrupados = defaultdict(list)
    for clube in clubes:
        agrupados[clube.serie].append(clube)

    return dict(agrupados)

# update clube
def update_clube(clube_id: int, clube_update: ClubesSchemaUpdate):
    stmt = select(Clubes).where(Clubes.id == clube_id)
    clube = session.execute(stmt).scalars().first()
    if clube is None:
        return {"error": "Equipe não encontrada"}

    for key, value in clube_update.model_dump().items():
        setattr(clube, key, value)
    session.commit()
    return {"Message": f'Clube {clube.nome} foi alterado com sucesso'}, 


# deletar clube
def deletar_clube(clube_id: int):
    stmt = select(Clubes).where(Clubes.id == clube_id)
    clube = session.execute(stmt).scalars().first()
    if stmt is None:
        return {"error": "Equipe nao encontrada"}
    session.delete(clube)
    session.commit()
    return {"Message": "Clube deletado com sucesso"}



def ler_dados():
    with open(file_path) as file:
        data = json.load(file)
    equipes = data['clubes']
    for i, time in enumerate(equipes):
        criar_clube(time['nome'], time['serie'], time['escudo'])
    return equipes



## cadastrar equipes
"""
with open(file_path,'r',encoding='utf-8') as file:
    data = json.load(file)
    equipes = data['clubes']
    for time in equipes:
        criar_clube(time['nome'], time['serie'], time['escudo'], time['estadio'], time['cidade'], time['sigla'])
"""


# atualizar_dados('Cuiabá', 'Fluminense', 0, 1)