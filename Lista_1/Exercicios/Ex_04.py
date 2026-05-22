# → Verificar se existe algum número ímpar
# que aparece um número ímpar de vezes na lista

v = [9,2,7,7,2,2,1,7,7,9]

i = 0

while i < len(v):
    cont = 0
    j = 0
    while j < len(v):
        if v[j] % 2 != 0:
            if v[i] == v[j]:
                cont += 1
                num = v[j]
        j += 1
    if cont % 2 != 0:
        print(f"Sim, o {v[i]}")
    i += 1