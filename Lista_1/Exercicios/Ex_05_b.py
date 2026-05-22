# Verificar se existem dois elementos na lista L tais que
# um deles é o dobro do outro

v = [9,42,21,144,25,3,19,33,45,6]
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

i = 0
while i < len(v):
    j = 0
    while j < len(v):
        if i != j and v[i] * 2 == v[j]:
            print(f"Sim, os números {v[i]} e {v[j]}")
        j += 1
    i += 1 