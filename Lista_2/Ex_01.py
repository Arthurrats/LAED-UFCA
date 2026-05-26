v = [9,42,21,14,25,3,19,33,45,6]

pMaior = 0
sMaior = 0
tMaior = 0
i = 0 

while i < len(v):
    mAtual = v[i]
    if mAtual > pMaior:
        tMaior = sMaior
        sMaior = pMaior
        pMaior = mAtual
    elif mAtual < pMaior and mAtual > sMaior:
        tMaior = sMaior
        sMaior = mAtual
    elif mAtual < sMaior and mAtual > tMaior:
        tMaior = mAtual
    i += 1

print(f"O teceiro maior número da lista é: {tMaior}")

# Tempo de execução: o(n)