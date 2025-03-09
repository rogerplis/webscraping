"use client";
import { Form,FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "@/components/ui/input";
import {  useForm } from "react-hook-form";
import { z } from "zod";
import { Button } from "@/components/ui/button";
import {useEffect, useState} from "react";

export const formSchema = z.object({
    rodada: z.coerce.number(),
    mandante: z.string(),
    visitante: z.string(),
    golsMandante: z.number(),
    golsVisitante: z.number(),
    dataJogo: z.string(),
    localJogo: z.string(),
    horaJogo: z.string(),
    
});
export const updateFormSchema = formSchema.extend({
    id: z.coerce.number(),
});

export type FormValues =
    z.infer<typeof formSchema> | z.infer<typeof updateFormSchema>;

interface FormJogoProps{
    initialValues?: FormValues;
    isUpdate?: boolean;
    onSuccess?: () => void;
    onAdd?: (values: z.infer<typeof formSchema>) => Promise<void>;
    onUpdate?: (values: z.infer<typeof updateFormSchema>) => Promise<void>;
}

export const FormJogo: React.FC<FormJogoProps>=({initialValues, isUpdate, onSuccess, onAdd, onUpdate}) => {
    const form = useForm<FormValues>({
        resolver: zodResolver(isUpdate ? updateFormSchema : formSchema),
        defaultValues: {
            rodada: 1,
            mandante: "",
            visitante: "",
            golsMandante: 0,
            golsVisitante: 0,
            dataJogo: "",
            localJogo: "",
            horaJogo: "",
            ...(initialValues || {}),
        },
    })
    const [isSubmitting, setisSubmitting] = useState<boolean>(false);
    const [submitError, setSubmitError] = useState<string | null>(null);

    useEffect(() => {
        if(initialValues){
            form.reset(initialValues);
        }
    }, [initialValues,form]);

    async function onSubmit(values: z.infer<typeof formSchema>) {
        setisSubmitting(true);
        setSubmitError(null);

        try {
            if (isUpdate) {
                if(onUpdate){
                    await onUpdate(values as z.infer<typeof updateFormSchema>);
                    form.reset();
                    onSuccess?.();
                } else {
                    throw new Error("onUpdate function is not defined")
                }


            } else {
                if(onAdd){
                    await onAdd(values as z.infer<typeof formSchema> );
                    form.reset();
                    onSuccess?.();
                } else {
                    throw new Error("onAdd function is not defined")
                }
            }

        }  catch (error:unknown) {
            let errorMessage = "An error ocurred while submitting the form";
            if (error instanceof Error) {
                console.error(error.message);
                errorMessage = error.message;
            } else {
                console.error("An unknown error occurred", error);
                errorMessage = "An unknown error occurred";
            }
            setSubmitError(errorMessage);
        } finally {
            setisSubmitting(false);
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
            {submitError && <p className="text-red-500">{submitError}</p>}
            <Button variant={"default"} type="submit" disabled={isSubmitting}>
                {isSubmitting ? "Enviando..." : isUpdate ? "Atualizar" : "Adicionar"}
            </Button>
        </form>
        </Form>
     );
}
 
export default FormJogo;
