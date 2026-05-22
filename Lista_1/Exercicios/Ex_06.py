# → Encontrar os dois elementos da lista L que possuem a menor diferen¸ca entre si
# — (em valor absoluto)

v = [9,2,7,7,2,2,1,7,7,9]
v1 = 0
v2 = 0
i = 0
menorDif = v[0] - v[1]

while i < len(v):
    j = 0
    difAtual = 0
    while j < len(v):
        if v[i] != v[j]:
            difAtual = v[i] - v[j]
            if difAtual < 0:
                difAtual *= (-1)
            if difAtual < menorDif:
                menorDif = difAtual
                v1 = v[i]
                v2 = v[j]
        j += 1
    i +=1

print(f"Os elementos: {v1} e {v2}")