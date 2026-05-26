v = [2,1,9,7,6,3,9,4,2,6,1,3]

i = 0
k = 4

while i < len(v):
    if v[i] == v[i+k]:
        print(f"Sim, o {v[i]} (nas posições {i} e {i+k})")
        break
    i += 1

# Tempo de execução: o(n).