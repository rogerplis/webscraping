import { Clubes } from "@/type";
import Image from "next/image";
import {Tooltip, TooltipContent, TooltipProvider, TooltipTrigger} from "@/components/ui/tooltip";

async function getClubes(): Promise<Clubes[]> {
    const response = await fetch('http://localhost:8585/clubes', {
        method: 'GET',
    next: {
        revalidate: 10,
    },
    cache: 'no-cache',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    const data = await response.json();
    console.log(data);
    const serieA = Array.isArray(data.serie_a) ? data.serie_a : []; 

    // Garantir q a resposta é um array
    return [...serieA];};

async function ClubesList()  {
    let clubes: Clubes[] = [];
    
    try {
        clubes = await getClubes();
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    } catch (error) {
        return <div>Erro ao carregar os clubes</div>;
    }
    // recupera os clubes da api
     
    console.log(clubes);
    return ( <div>
        <h1 className="text-2xl">Clubes Participantes</h1>
        <div className="grid grid-cols-4 gap-2 items-start ">
            {clubes.length === 0 ? (
                <div>Não há clubes cadastrados</div>
            ): (
                clubes.map(clube => (
                    <TooltipProvider key={clube.id}>
                         <Tooltip>
                             <TooltipTrigger>

                                 <div key={clube.id} className="flex items-center w-[250px] border-t border-b h-10 mt-2 p-2 gap-2">
                                     <div className="flex gap-2 items-center justify-start  m-1 text-sm">
                                         <Image
                                             src={`/serie_a/${clube.escudo}`}
                                             alt={clube.nome}
                                             width={40}
                                             height={40}
                                         />{" "}
                                     </div>

                                 </div>
                             </TooltipTrigger>
                             <TooltipContent>
                                 <span>{clube.nome}</span>
                             </TooltipContent>
                         </Tooltip>
                    </TooltipProvider>

                ))
            )
            }
        </div>
    </div>);
}

export default ClubesList;
