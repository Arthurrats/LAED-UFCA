v = [17, 2, 8, 1, 7, 13, 9, 12, 4, 16]

i = 0
while i < len(v):
    j = 0
    while j < len(v):
        if v[i] < v[j]:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
        j += 1
    i += 1

numero_isolado = None
i = 0

while i < len(v):
    isolado_esquerda = True
    isolado_direita = True
    
    if i > 0 and v[i-1] == v[i] - 1:
        isolado_esquerda = False
        
    if i < len(v) - 1 and v[i+1] == v[i] + 1:
        isolado_direita = False
        
    if isolado_esquerda and isolado_direita:
        numero_isolado = v[i]
        break         
    i += 1

print(f"Sim, o {numero_isolado}")

# Tempo de execução: o(n²)