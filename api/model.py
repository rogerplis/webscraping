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
    dataJogo = Column(String)
    horaJogo = Column(String)
    localJogo = Column(String)

    def __init__(self, rodada, mandante, visitante, golsMandante, golsVisitante, dataJogo, localJogo, horaJogo):
        self.rodada = rodada
        self.mandante = mandante
        self.visitante = visitante
        self.golsMandante = golsMandante
        self.golsVisitante = golsVisitante
        self.dataJogo = dataJogo
        self.localJogo = localJogo
        self.horaJogo = horaJogo


class Clubes(Base):
    __tablename__ = 'tb_clubes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    serie = Column(String)
    escudo = Column(String)
    estadio = Column(String)
    cidade = Column(String)
    sigla = Column(String)

    def __init__(self, nome, serie, escudo, estadio, cidade, sigla):
        self.nome = nome
        self.serie = serie
        self.escudo = escudo
        self.estadio = estadio
        self.cidade = cidade
        self.sigla = sigla


Base.metadata.create_all(engine)
