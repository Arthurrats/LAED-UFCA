u = [1,2,3,4,5,6,7,8,9,10]
v = [7,2,3,1,6,5,9,10,4,8]

i = 0
achei = True

if len(u) != len(v):
    achei = False
    print("Não há permutação entre as duas listas.")

while i < len(u):
    j = 0
    cont = 0
    while j < len(v):
        if u[i] == v[j]:
            cont += 1
            break
        j += 1
    if cont == 0:
        achei = False
        print("Não há permutação entre as duas listas.")
        break
    i += 1

if achei:
    print("Há permutação entre as duas listas.")

# Tempo de execução: o(n²)
