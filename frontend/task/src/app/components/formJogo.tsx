"use client";
import { Form,FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "@/components/ui/input";
import {  useForm } from "react-hook-form";
import { z } from "zod";
import { Button } from "@/components/ui/button";

const formSchema = z.object({
    rodada: z.coerce.number(),
    mandante: z.string(),
    visitante: z.string(),
    golsMandante: z.number(),
    golsVisitante: z.number(),
    dataJogo: z.string(),
    localJogo: z.string(),
    horaJogo: z.string(),
    
});

const FormJogo = () => {
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            rodada: 1,
            mandante: "",
            visitante: "",
            golsMandante: 0,
            golsVisitante: 0,
            dataJogo: "",
            localJogo: "",
            horaJogo: "",
        },
    })

    async function onSubmit(values: z.infer<typeof formSchema>) {
        try {
            const response = await fetch("http://localhost:8585/rodada/add", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
                
            });
            
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            
            const data = await response.json();
            console.log(data);
            
        } catch (error) {
            console.log(error);
        }        
        
      }


    return ( 
        <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6 items-center">
            <FormField
            control={form.control}
            name="rodada"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Rodada</FormLabel>
                <FormControl>
                    <Input placeholder="Rodada" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            <FormField
            control={form.control}
            name="mandante"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Mandante</FormLabel>
                <FormControl>
                    <Input placeholder="Mandante" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            <FormField
            control={form.control}
            name="visitante"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Visitante</FormLabel>
                <FormControl>
                    <Input placeholder="Visitante" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            {/* 
            
            <FormField
            control={form.control}
            name="golsMandante"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Gols Mandante</FormLabel>
                <FormControl>
                    <Input placeholder="Gols Mandante" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            <FormField
            control={form.control}
            name="golsVisitante"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Gols Visitante</FormLabel>
                <FormControl>
                    <Input placeholder="Gols Visitante" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            */}
            <FormField
            control={form.control}
            name="dataJogo"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Data Jogo</FormLabel>
                <FormControl>
                    <Input placeholder="Data Jogo" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            <FormField
            control={form.control}
            name="localJogo"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Local Jogo</FormLabel>
                <FormControl>
                    <Input placeholder="Local Jogo" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            <FormField
            control={form.control}
            name="horaJogo"
            render={({ field }) => (
                <FormItem>
                <FormLabel>Hora Jogo</FormLabel>
                <FormControl>
                    <Input placeholder="Hora Jogo" {...field} />
                </FormControl>
                <FormMessage />
                </FormItem>
            )}
            />
            <Button variant={"default"} type="submit">Submit</Button>
        </form>
        </Form>
     );
}
 
export default FormJogo;