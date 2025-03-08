from collections import defaultdict
import json
from pathlib import Path
from sqlalchemy.future import select
from api.model import Jogos
from api.schemas.jogosSchema import Jogo

from api.config import session

file_path = Path(__file__).parent.parent / "dados" / "dados.json"



"""Area de Jogos"""
def criar_jogo(rodada: int,
               mandante: str,
               visitante: str,
               golsMandante: int,
               golsVisitante: int,
               dataJogo: str,
               localJogo: str,
               horaJogo: str):
    jogo = Jogos(rodada=rodada, mandante=mandante, visitante=visitante, golsMandante=golsMandante,
                 golsVisitante=golsVisitante, dataJogo=dataJogo, localJogo=localJogo, horaJogo=horaJogo)
    session.add(jogo)
    session.commit()
    return {"Message": "Jogo criado com sucesso"}


def get_all_jogos_por_rodada(rodada: int):    
    stmt = select(Jogos).where(Jogos.rodada == rodada)        
    return session.execute(stmt).scalars().all()


def get_jogo_all():
    stmt = select(Jogos)
    stmt = stmt.group_by(Jogos)
    return session.execute(stmt).scalars().all()


def get_jogo_por_equipe(equipe: str):
    stmt = select(Jogos).where(Jogos.mandante == equipe or Jogos.visitante == equipe)
    return session.execute(stmt).scalars().all()

def get_jogo(id: int):
    stmt = select(Jogos).where(Jogos.id == id)
    return session.execute(stmt).scalars().first()