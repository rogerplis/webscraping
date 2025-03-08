'use client'
import { useRouter } from "next/navigation";
import { z } from "zod";
import { FormJogo, formSchema } from "@/app/components/formJogo";


const AddJogoPage: React.FC = () => {
    const router = useRouter();
    const handleAdd = async (values: z.infer<typeof formSchema>): Promise<void> => {
        try {
            const response = await fetch("http://localhost:8585/rodada/add", {
                method: "POST",
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
            console.log("jogo adicionado: ", data);
            router.push("/")
        } catch (error) {
            console.error("Erro ao adicionar jogo", error);
            if (error instanceof Error) {
                alert(error.message || "Erro ao adicionar jogo");
            } else {
                alert("Erro ao adicionar jogo");
            }
        }
    };
    const handleSuccess = () => {
        router.push("/");
    };


    return (
        <FormJogo onAdd={handleAdd} onSuccess={handleSuccess} />
    );
}
 
export default AddJogoPage;
