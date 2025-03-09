from pydantic import BaseModel, computed_field


from api.util import remover_acentos


class Jogo(BaseModel):
    rodada: int
    mandante: str
    visitante: str
    golsMandante: int
    golsVisitante: int
    dataJogo: str
    localJogo: str
    horaJogo: str

class JogoResponse(BaseModel):
    id: int
    rodada: int
    mandante: str    
    visitante: str      
    golsMandante: int
    golsVisitante: int
    localJogo: str    
    horaJogo: str
    dataJogo: str

    @computed_field
    def mandanteEscudo(self) -> str:
        if self.mandante is None:
            return ""
        escudoMandante = remover_acentos(self.mandante)
        return escudoMandante

    @computed_field
    def visitanteEscudo(self) -> str:
        if self.visitante is None:
            return ""
        escudoVisitante = remover_acentos(self.visitante)
        return escudoVisitante
    
    def dict(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        data['escudoMandante'] = self.mandanteEscudo
        data['escudoVisitante'] = self.visitanteEscudo       
        
        return data

class JogoUpdate(BaseModel):
        id: int
        rodada: int
        mandante: str
        visitante: str
        golsMandante: int
        golsVisitante: int
        dataJogo: str
        localJogo: str
        horaJogo: str
