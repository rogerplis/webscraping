from typing import Dict, List
from pydantic import BaseModel



class ClassificacaoUpdate(BaseModel):
    equipe: str
    pontos: int
    jogos: int
    vitorias: int
    empates: int
    derrotas: int
    golsPro: int
    golsContra: int
    saldoGols: int






class UpdateClassificacao(BaseModel):
    mandante: str
    visitante: str
    golsMandante: int
    golsVisitante: int


