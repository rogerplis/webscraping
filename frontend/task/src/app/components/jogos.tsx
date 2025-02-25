"use client";
import Image from "next/image";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useState } from "react";
import JogoRodada from "./jogo";

const Jogos = () => {
  const [rodada, setRodada] = useState(1);
  const handleRodada = (rodada: number) => {
    setRodada(rodada);
  };
  const mandante = "Bahia";
  const visitante = "Corinthians";
  const golsMandante = 0;
  const golsVisitante = 0;
  const dataJogo = "A definir";
  const localJogo = "A definir";
  const horaJogo = "A definir";
  const escudoMandante = `/serie_a/${mandante.toLowerCase()}.svg`;
  const escudoVisitante = `/serie_a/${visitante.toLowerCase()}.svg`;

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
      <JogoRodada
        rodada={0}
        mandante={mandante}
        visitante={visitante}
        golsMandante={golsMandante}
        golsVisitante={golsVisitante}
        dataJogo={dataJogo}
        localJogo={localJogo}
        horaJogo={horaJogo}
        escudoMandante={escudoMandante}
        escudoVisitante={escudoVisitante}
        
      />
      <div className="flex flex-col items-center border-t mt-1 p-2">
        <span>30/03/2025 19:00</span>
        <span> Fonte Nova - Salvador</span>
        <div className="flex gap-2 items-center">
          <div className="flex gap-2 items-center justify-end w-[180px] m-1 text-lg">
            Flamengo{" "}
            <Image
              src="/serie_a/flamengo.svg"
              alt="Flamengo"
              width={40}
              height={40}
            />{" "}
          </div>
          <span className="text-center text-3xl">0</span>
          <span className="text-center text-3xl">x</span>
          <span className="text-center text-3xl">0</span>
          <div className="flex gap-2 items-center justify-start w-[180px] m-1 text-lg">
            {" "}
            <Image
              src="/serie_a/internacional.svg"
              alt="Internacional"
              width={40}
              height={40}
            />{" "}
            Internacional{" "}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Jogos;
