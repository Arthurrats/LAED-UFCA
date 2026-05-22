# → Procurar o n´umero k na lista L, e se ele não estiver lá
# retornar o elemento da lista com o valor mais próximo de k

v = [9,42,21,14,25,3,19,33,45,6]

k = 31
i = 0
num = v[0]

while i < len(v):
    numAtual = 0
    if v[i] == k:
        print(f"Achei o valor: {k}")
    numAtual = k - v[i]
    if numAtual < 0:
        numAtual = numAtual * (-1)
    if numAtual < num:
        num = numAtual
        pos = i
    i += 1

print(f"Não está lá, mas eu encontrei o {pos}")