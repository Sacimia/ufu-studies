n = int(input("Insere uma quantidade de linha: "))
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(n):
        if i == j:
            print(1)
        else:
            print(0)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print("\n")
