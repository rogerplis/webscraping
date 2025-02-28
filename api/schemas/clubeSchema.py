from typing import Dict, List
from pydantic import BaseModel


class ClubesSchema(BaseModel):
    nome: str
    serie: str
    escudo: str
    sigla: str
    estadio: str
    cidade: str


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
    sigla: str
    estadio: str
    cidade: str