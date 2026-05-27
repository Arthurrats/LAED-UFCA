M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [9, 0, 1, 2]
]

linhas_como_tuplas = [tuple(linha) for linha in M]

if len(linhas_como_tuplas) > len(set(linhas_como_tuplas)):
    print("Sim, a matriz contém duas linhas exatamente iguais")
else:
    print("Não existem linhas repetidas")