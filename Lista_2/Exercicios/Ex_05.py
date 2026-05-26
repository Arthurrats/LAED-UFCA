v = [7,1,9,1,7,3,9,2,1,6,8,3]

i = 0
k = 3
while i < len(v):
    cont = 0
    j = 0
    while j < len(v):
        if v[i] == v[j]:
            cont += 1
            num = v[i]
        j += 1
    if cont == k:
        print(f"Sim, o {num}")
        break
    i += 1

# Tempo de execução: o(n²).