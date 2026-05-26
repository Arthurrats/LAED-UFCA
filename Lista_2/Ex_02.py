v = [9,42,21,14,25,3,19,33,45,6]

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

k = 4

print(f"O {k} maior número dá lista é: {v[4]}")

# Tempo de execução: o(n²)