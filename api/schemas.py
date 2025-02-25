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



class Jogo(BaseModel):
    rodada: int
    mandante: str
    visitante: str
    golsMandante: int
    golsVisitante: int
    dataJogo: str
    localJogo: str
    horaJogo: str


class UpdateClassificacao(BaseModel):
    mandante: str
    visitante: str
    golsMandante: int
    golsVisitante: int


class ClubesSchema(BaseModel):
    nome: str
    serie: str
    escudo: str
    sigla: str


    def __init__(self, **data):
        super().__init__(**data)

    class Config:
        from_attributes = True

class ClubesAgrupados(BaseModel):
    clubes: Dict[str, List[ClubesSchema]]
    
    
class ClubesSchemaUpdate(BaseModel):
    nome: str
    serie: str
    escudo: str