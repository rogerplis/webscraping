from typing import List
from fastapi import APIRouter

from api.schemas.jogosSchema import Jogo, JogoResponse
from services.jogoService import criar_jogo, get_all_jogos_por_rodada, get_jogo

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

@router.get('/jogo/{id}',response_model=JogoResponse)
def get_jogorodada(id: int):
    jogo = get_jogo(id)
    return jogo