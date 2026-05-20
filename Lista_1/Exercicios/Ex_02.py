v = [9,42,21,14,28,3,19,32,46,6]

v = [9,42,21,14,28,3,19,32,46,6]

i = 0
pMaiorImpar = v[0]
sMaiorImpar = 0

while i < len(v):
    if v[i] % 2 != 0:
        if v[i] > pMaiorImpar:
            sMaiorImpar = pMaiorImpar
            pMaiorImpar = v[i]
        elif v[i] < pMaiorImpar and v[i] > sMaiorImpar:
            sMaiorImpar = v[i]
    i += 1

print(f"O maior número ímpar é: {sMaiorImpar}")