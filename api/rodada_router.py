from typing import List
from fastapi import APIRouter

from schemas.jogosSchema import Jogo, JogoResponse
from services.jogoService import criar_jogo, get_all_jogos_por_rodada


router = APIRouter(prefix='/rodada', tags=['rodada'])

@router.get('/{rodada}', response_model=List[JogoResponse])
def get_rodada(rodada: int):    
    jogos = get_all_jogos_por_rodada(rodada)
    return [jogo for jogo in jogos] 

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