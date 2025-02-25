export interface Jogo {
    rodada: number
    mandante: string
    visitante: string
    golsMandante: number
    golsVisitante: number
    dataJogo: string
    localJogo: string
    horaJogo: string
    escudoMandante: string
    escudoVisitante: string
  }

export interface Clubes {
    id: number
    nome: string
    serie: string
    escudo: string
  }