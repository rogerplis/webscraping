"use client";
import { ChevronLeft, ChevronRight } from "lucide-react";
import {  useEffect, useState } from "react";
import JogoRodada from "./jogo";
import { Jogo } from "@/type";

const Jogos = () => {
  const [rodada, setRodada] = useState(1);
  const [jogos, setJogos] = useState<Jogo[]>([]);
  const handleRodada = (rodada: number) => {
    setRodada(rodada);
  };
  useEffect(() => {
    const fetchJogos = async () => {
      try {
        const response = await fetch(`http://localhost:8585/rodada/${rodada}`);
        const data = await response.json();
        setJogos(data);
      } catch (error) {
        console.error("Error fetching jogos:", error);
      }
    };
    fetchJogos();
  }, [rodada]);  



  return (
    <div className="flex flex-col items-center gap-1">
      <h1 className="text-3xl">Jogos</h1>
      <div className="flex items-center border-t mt-2 p-2 gap-2">
        <ChevronLeft
          onClick={rodada > 1 ? () => handleRodada(rodada - 1) : undefined}
          className={
            rodada === 1 ? "cursor-not-allowed text-gray-600" : "text-green-600"
          }
        />
        <span className="text-2xl">rodada {rodada} de 38</span>
        <ChevronRight
          onClick={rodada < 38 ? () => handleRodada(rodada + 1) : undefined}
          className={
            rodada === 38
              ? "cursor-not-allowed text-gray-600"
              : "text-green-600"
          }
        />
      </div>
      {jogos.map((jogo) => (
        <JogoRodada
          key={jogo.id}
          id={jogo.id}
          mandante={jogo.mandante}
          visitante={jogo.visitante}
          golsMandante={jogo.golsMandante}
          golsVisitante={jogo.golsVisitante}
          dataJogo={jogo.dataJogo}
          localJogo={jogo.localJogo}
          horaJogo={jogo.horaJogo}
          mandanteEscudo={`/serie_a/${jogo.mandanteEscudo}.svg`}
          visitanteEscudo={`/serie_a/${jogo.visitanteEscudo}.svg`}         />
      ))}     
     
    </div>
  );
};

export default Jogos;
