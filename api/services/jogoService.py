from collections import defaultdict
import json
from pathlib import Path

from fastapi import HTTPException
from sqlalchemy.future import select
from api.model import Jogos
from api.schemas.jogosSchema import JogoUpdate

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

def atualizar_jogo(id_jogo: int, jogo: JogoUpdate):
    # Recupera o jogo da sessão diretamente, garantindo que ele seja associado à sessão
    jogo_update = session.get(Jogos, id_jogo)

    if jogo_update is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    # Atualiza os campos do jogo com base no modelo
    for key, value in jogo.model_dump().items():
        setattr(jogo_update, key, value)

    try:
        # Confirma que o objeto já existe na sessão antes de tentar realizar o commit
        session.merge(jogo_update)  # Força a sessão a reconhecer o objeto
        session.commit()          # Comita as alterações
        session.refresh(jogo_update)  # Atualiza o objeto com os dados mais recentes após o commit
    except Exception as e:
        # Se houver um erro durante o commit, podemos tratar de forma apropriada
        session.rollback()
        raise HTTPException(status_code=500, detail="Erro ao atualizar o jogo")

    return jogo_update


update_data = JogoUpdate(

        id=12,
        rodada= 1,
        mandante= "Bahia",
        visitante= "Corinthians",
        golsMandante= 0,
        golsVisitante= 0,
        localJogo= "Casa de Apostas Arena Fonte Nova",
        horaJogo="21:31",
        dataJogo= "29/03/2025"

)

#atualizar_jogo(update_data.id, update_data)