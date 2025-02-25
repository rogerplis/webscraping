from fastapi import APIRouter

from schemas import Jogo
from services import criar_jogo, get_all_jogos_por_rodada


router = APIRouter(prefix='/rodada', tags=['rodada'])

@router.get('/{rodada}')
def get_rodada(rodada: int):
    rodada = get_all_jogos_por_rodada(rodada)
    return rodada

@router.post('/add')
def add_rodada(jogo: Jogo):
    criar_jogo(jogo.rodada, jogo.mandante,
               jogo.visitante, 
               jogo.golsMandante, 
               jogo.golsVisitante, 
               jogo.dataJogo,
               jogo.localJogo,
               jogo.horaJogo)
    return jogo