U = [1, 12, 15, 26]
V = [2, 13, 17, 30]

i = 0
j = 0

salto = len(U) // 2

while salto > 0:
    if U[i + salto] < V[j + salto]:
        i += salto 
    else:
        j += salto
        
    salto //= 2

mediana = max(U[i], V[j])

print(f"A mediana combinada é: {mediana}")