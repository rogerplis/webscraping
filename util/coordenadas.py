from itertools import permutations
from geopy.distance import geodesic

# Lista de coordenadas das cidades
coordenadas = {
    "São Paulo": (-23.55052, -46.633308),
    "Rio de Janeiro": (-22.906847, -43.172897),
    "Aparecida": (-22.847293227456824, -45.23051563376285),
    "Curitiba": (-25.428356, -49.273251),
    "Porto Alegre": (-30.034647, -51.217658),
    "Brasília": (-15.826691, -47.921822),
    "Salvador": (-12.971399, -38.501221),
    "Recife": (-8.047562, -34.877011),
    "Campo Grande": (-20.475291098829928, -54.63450740783154)
}

# Gerar todas as permutações possíveis das cidades intermediárias
cidades_intermediarias = ["Curitiba", "Brasília","Porto Alegre", "Recife", "Salvador", "Aparecida", "Rio de Janeiro", "Campo Grande"]
melhor_rota = None
menor_distancia = float("inf")

# Testar todas as ordens possíveis das cidades intermediárias
for perm in permutations(cidades_intermediarias):
    rota_teste = ["São Paulo"] + list(perm) + ["São Paulo"]
    distancia_teste = sum(
        geodesic(coordenadas[rota_teste[i]], coordenadas[rota_teste[i + 1]]).kilometers
        for i in range(len(rota_teste) - 1)
    )
    
    # Atualizar se encontrar uma rota menor
    if distancia_teste < menor_distancia:
        menor_distancia = distancia_teste
        melhor_rota = rota_teste

# Exibir a melhor rota e a menor distância
print("Melhor rota:", " -> ".join(melhor_rota))
print("Distância total:", round(menor_distancia, 2), "km")
