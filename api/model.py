from sqlalchemy import Column, Integer, String

from con import Base, engine


class Classifications(Base):
    __tablename__ = 'tb_classifications'
    id = Column(Integer, primary_key=True)
    equipe = Column(String)
    jogos = Column(Integer)
    vitorias = Column(Integer)
    empates = Column(Integer)
    derrotas = Column(Integer)
    golsPro = Column(Integer)
    golsContra = Column(Integer)
    saldoGols = Column(Integer)
    pontos = Column(Integer)

    def __init__(self, equipe, jogos, vitorias, empates, derrotas,
                 golsPro, golsContra, saldoGols, pontos):
        self.equipe = equipe
        self.jogos = jogos
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas
        self.golsPro = golsPro
        self.golsContra = golsContra
        self.saldoGols = saldoGols
        self.pontos = pontos



class Jogos(Base):
    __tablename__ = 'tb_jogos'
    id = Column(Integer, primary_key=True)
    rodada = Column(Integer)
    mandante = Column(String)
    visitante = Column(String)
    golsMandante = Column(Integer)
    golsVisitante = Column(Integer)

    def __init__(self, rodada, mandante, visitante, golsmandante, golsvisitante):
        self.rodada = rodada
        self.mandante = mandante
        self.visitante = visitante
        self.golsMandante = golsmandante
        self.golsVisitante = golsvisitante


class Clubes(Base):
    __tablename__ = 'tb_clubes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    serie = Column(String)
    escudo = Column(String)

    def __init__(self, nome, serie, escudo):
        self.nome = nome
        self.serie = serie
        self.escudo = escudo


Base.metadata.create_all(engine)
