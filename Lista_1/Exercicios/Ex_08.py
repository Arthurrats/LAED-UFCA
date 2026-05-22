# → Imprimir todos os n´umeros que aparecem nas duas listas

u = [9,2,7,7,2,2,1,7,7,9]
v = [2,15,19,12,33,9,17,41,54,8]
i = 0

while i < len(u):
    apareceu = False
    j = 0
    while j < i:
        if u[i] == u[j]:
            apareceu = True
        j += 1
    
    if not apareceu:
        j = 0
        while j < len(v):
            if u[i] == v[j]:
                print(u[i], end=" ")
                j = len(v)
            j += 1
    i += 1