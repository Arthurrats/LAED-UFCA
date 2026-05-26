v = [5,3,1,10,2,13,9,12,4,7]

media = 0
i = 0
cont = 0

while i < len(v):
    media += v[i]
    cont += 1
    i += 1

media = media/cont

i = 0 
nProx = v[1]

while i < len(v):
    nAtual = media - v[i]
    if nAtual < 0:
        nAtual *= (-1)
    if nAtual < nProx:
        nProx = nAtual
        num = v[i]
    i +=1 

print(f"O número mais próxima da média {media} é {num}.")

# Tempo de execução: o(n).