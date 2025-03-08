export interface Jogo {
    id: number | null | undefined        
    mandante: string
    visitante: string
    golsMandante: number
    golsVisitante: number
    dataJogo: string
    localJogo: string
    horaJogo: string
    mandanteEscudo: string
    visitanteEscudo: string
  }

  export interface JogoAdd {
    rodada: number
    mandante: string
    visitante: string
    golsMandante: number
    golsVisitante: number
    dataJogo: string
    localJogo: string
    horaJogo: string    
  }
  export interface JogoUpdate {
    id: number | null | undefined 
    rodada: number
    mandante: string
    visitante: string
    golsMandante: number
    golsVisitante: number
    dataJogo: string
    localJogo: string
    horaJogo: string    
  }

export interface Clubes {
    id: number
    nome: string
    serie: string
    escudo: string
  }