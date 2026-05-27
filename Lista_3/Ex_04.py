M = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 4, 16]
]

todos_numeros = [num for linha in M for num in linha]

if len(todos_numeros) > len(set(todos_numeros)):
    print("Sim, existem elementos que aparecem mais de uma vez")
else:
    print("Não existem elementos repetidos")