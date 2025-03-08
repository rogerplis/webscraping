'use client'

import { JogoUpdate} from "@/type";
import {useEffect, useState} from "react";
import {FormJogo, updateFormSchema} from "@/app/components/formJogo";
import { useParams, useRouter } from "next/navigation";
import {z} from "zod";


export default function EditJogoPage() {
    const router = useRouter();
    const {id} = useParams();
    const [initialValues, setInitialValues] = useState<JogoUpdate | null>(null);

    useEffect(() => {
            const fetchJogo = async () => {
                try {
                    const response = await fetch(`http://localhost:8585/rodada/jogo/${id}`,);
                    if (!response.ok) {
                        throw new Error("Could not fetch Jogo");
                    }
                    const data = await response.json();
                    setInitialValues(data);
                } catch (error) {
                    console.error(error);
                    alert("Erro ao buscar dados do jogo");
                    router.push("/");
                }
            };
            fetchJogo();
        }, [id, router]
    )


    const handleUpdate = async (values: z.infer<typeof updateFormSchema>) => {
        try {
            const response = await fetch(`http://localhost:8585/rodada/update/${values.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            });
            if (!response.ok) {
                const errorData = await response.json();
                const errorMessage = errorData.detail || "Erro na resposta do servidor"
                throw new Error(errorMessage);
            }
            const data = await response.json();
            console.log("jogoatualizado: ", data);
            router.push("/")
        } catch (error)  {
            console.error("Erro ao atualizar jogo", error);
            if (error instanceof Error) {
                alert(error.message || "Erro ao atualizar jogo");
            } else {
                alert("Erro ao atualizar jogo");
            }
        }
    };
    const handleSuccess = () =>{
        router.push("/");
    }
    console.log(initialValues)
    return (
        <div>
            <h1 className="text-2xl font-bold mb-4"> Editarjogo</h1>
            {initialValues && (
                <FormJogo
                    initialValues={initialValues}
                    isUpdate={true}
                    onUpdate={handleUpdate}
                    onSuccess={handleSuccess}
                />
            )}
        </div>
    );
    }
