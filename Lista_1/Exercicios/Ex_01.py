# → Encontrar o maior n´umero ´ımpar armazenado na lista — (se houver algum)

v = [9,42,21,14,28,3,19,32,46,6]

i = 0
maiorImpar = v[0]

while i < len(v):
    if v[i] % 2 != 0:
        if v[i] > maiorImpar:
            maiorImpar = v[i]
    i += 1

print(f"O maior número ímpar é: {maiorImpar}")