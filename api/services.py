import json

from sqlalchemy.future import select
from api.model import Classifications, Jogos, Clubes
from api.schemas import ClassificacaoUpdate, Jogo, UpdateClassificacao

from con import session

file_path = '../dados/dados.json'


def get_classifications():
    stmt = select(Classifications)
    stmt = stmt.order_by(Classifications.pontos.desc(), Classifications.vitorias.desc(),
                         Classifications.saldoGols.desc(), Classifications.equipe.asc())
    return session.execute(stmt).scalars().all()


def criar_classificacao(equipe, jogos, vitorias, empates, derrotas, golsPro, golsContra, saldoGols,
                        pontos, aproveitamento, position):
    classification = Classifications(equipe, jogos, vitorias, empates, derrotas, golsPro, golsContra, saldoGols, pontos,
                                     aproveitamento, position)
    session.add(classification)
    session.commit()
    return classification


def update_classificacao(equipe_id: int, classsificacao_update: ClassificacaoUpdate):
    stmt = select(Classifications).where(Classifications.id == equipe_id)
    classification = session.execute(stmt).scalars().first()
    if stmt is None:
        return {"error": "Equipe não encontrada"}

    for key, value in classsificacao_update.dict().items():
        setattr(classification, key, value)
    session.commit()
    return classification


def criar_clube(nome: str, serie: str, escudo: str):
    clube = Clubes(nome=nome, serie=serie, escudo=escudo)
    session.add(clube)
    session.commit()
    return clube


def get_all_clubes():
    stmt = select(Clubes)
    stmt = stmt.order_by(Clubes.nome.asc())
    return session.execute(stmt).scalars().all()


def criar_jogo(rodada: int,
               mandante: str,
               visitante: str,
               golsMandante: int,
               golsVisitante: int):
    jogo = Jogos(rodada=rodada, mandante=mandante, visitante=visitante, golsmandante=golsMandante,
                 golsvisitante=golsVisitante)
    session.add(jogo)
    session.commit()
    return {"Message": "Jogo criado com sucesso"}


def improvement(vitorias, empates, jogos):
    return ((vitorias * 3) + empates) / (jogos * 3) * 100


def atualizar_dados(mandante: str, visitante: str, golsMandante, golsVisitante):
    time_a = mandante
    time_b = visitante
    gols_a = golsMandante
    gols_b = golsVisitante
    stmt = select(Classifications).where(Classifications.equipe == time_a)
    equipe_a = session.execute(stmt).scalars().first()
    stmt = select(Classifications).where(Classifications.equipe == time_b)
    equipe_b = session.execute(stmt).scalars().first()
    if equipe_a is None or equipe_b is None:
        return {"error": "Equipe não encontrada"}
    equipe_a.jogos += 1
    equipe_a.golsPro += gols_a
    equipe_a.golsContra += gols_b
    equipe_a.saldoGols += gols_a - gols_b
    if gols_a > gols_b:
        equipe_a.vitorias += 1
        equipe_a.pontos += 3
    elif gols_a == gols_b:
        equipe_a.empates += 1
        equipe_a.pontos += 1
    else:
        equipe_a.derrotas += 1
    equipe_b.jogos += 1
    equipe_b.golsPro += gols_b
    equipe_b.golsContra += gols_a
    equipe_b.saldoGols += gols_b - gols_a
    if gols_b > gols_a:
        equipe_b.vitorias += 1
        equipe_b.pontos += 3
    elif gols_a == gols_b:
        equipe_b.empates += 1
        equipe_b.pontos += 1
    else:
        equipe_b.derrotas += 1
    session.commit()
    return {"message": "Dados atualizados com sucesso"}


def update_classificacao2(eqpe: str, jogos: int, vitorias: int, empates: int, derrotas: int, golsPro: int,
                          golsContra: int, saldoGols: int, pontos: int):
    stmt = select(Classifications).where(Classifications.equipe == eqpe)
    classsificacao_update = ClassificacaoUpdate(equipe=eqpe, jogos=jogos, vitorias=vitorias, empates=empates,
                                                derrotas=derrotas, golsPro=golsPro, golsContra=golsContra,
                                                saldoGols=saldoGols,
                                                pontos=pontos)
    classification = session.execute(stmt).scalars().first()
    if stmt is None:
        return {"error": "Equipe não encontrada"}

    for key, value in classsificacao_update.dict().items():
        setattr(classification, key, value)
    session.commit()
    return classification


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


def ler_dados():
    with open(file_path) as file:
        data = json.load(file)
    equipes = data['clubes']
    for i, time in enumerate(equipes):
        criar_clube(time['nome'], time['serie'], time['escudo'])
    return equipes


def resetar_classificacao():
    stmt = select(Classifications)
    classificacao = session.execute(stmt).scalars().all()
    for i in classificacao:
        i.jogos = 0
        i.vitorias = 0
        i.empates = 0
        i.derrotas = 0
        i.golsPro = 0
        i.golsContra = 0
        i.saldoGols = 0
        i.pontos = 0
        i.aproveitamento = 0
    session.commit()
    return {"message": "Classificação resetada com sucesso"}


def somatorio_por_clube(clube: str, j: Jogo):  # clubes = get_all_clubes() jogos = get_all_jogos_por_rodada(1)
    jg = 0
    gp = 0
    gc = 0
    sg = 0
    v = 0
    e = 0
    d = 0
    p = 0

    if clube == j.mandante:
        jg += 1
        gp += j.golsMandante
        gc += j.golsVisitante
        sg += j.golsMandante - j.golsVisitante
        if j.golsMandante > j.golsVisitante:
            v += 1
            p += 3
        elif j.golsMandante == j.golsVisitante:
            e += 1
            p += 1
        else:
            d += 1
    if clube == j.visitante:
        jg += 1
        gp += j.golsVisitante
        gc += j.golsMandante
        sg += j.golsVisitante - j.golsMandante
        if j.golsVisitante > j.golsMandante:
            v += 1
            p += 3
        elif j.golsVisitante == j.golsMandante:
            e += 1
            p += 1
        else:
            d += 1
    update_classificacao2(clube, jogos=jg, vitorias=v, empates=e, derrotas=d, golsPro=gp, golsContra=gc,
                          saldoGols=sg,
                          pontos=p)
    session.commit()

    return {"message": "Dados atualizados com sucesso"}


"""
with open(file_path,'r',encoding='utf-8') as file:
    data = json.load(file)
    equipes = data['clubes']
    for time in equipes:
        criar_clube(time['nome'], time['serie'], time['escudo'])
"""
# atualizar_dados('Cuiabá', 'Fluminense', 0, 1)




