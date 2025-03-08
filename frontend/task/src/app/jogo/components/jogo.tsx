import { Jogo } from "@/type";
import Image from "next/image";

const JogoRodada = (jogo: Jogo) => {
    
    return (  <div className="flex flex-col items-center border-t mt-1 p-2">
            <span>{jogo.dataJogo + " " + jogo.horaJogo}</span>
            <span> {jogo.localJogo}</span>
            <div className="flex gap-2 items-center">
              <div className="flex gap-2 items-center justify-end w-[180px] m-1 text-lg">
                {jogo.mandante}{" "}
                <Image
                  src={jogo.mandanteEscudo}
                  alt={jogo.mandante}
                  width={40}
                  height={40}
                />
              </div>
              <span className="text-center text-3xl">{jogo.golsMandante}</span>
              <span className="text-center text-3xl">x</span>
              <span className="text-center text-3xl">{jogo.golsVisitante}</span>
              <div className="flex gap-2 items-center justify-start w-[180px] m-1 text-lg">
                
                <Image
                  src={jogo.visitanteEscudo}
                  alt={jogo.visitante}
                  width={40}
                  height={40}
                />
                {jogo.visitante}
              </div>
            </div>
          </div>);
}
 
export default JogoRodada;