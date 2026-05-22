# Nos dizemos que o par de elementos V[i] e V[j] formam uma inversão se
# i < j e V[i] > V[j]

# A tarefa consiste em:
# → Contar o n´umero de invers˜oes na lista V

v = [9,2,7,7,2,2,1,7,7,9]
i = 0 
cont = 0
while i < len(v):
    j = i + 1
    while j < len(v):
        if v[i] > v[j]:
            cont += 1
        j += 1
    i += 1

print(f"{cont} inversões.")