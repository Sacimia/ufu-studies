matriz_progomal = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

num_linha = len(matriz_progomal)
num_colunas = len(matriz_progomal)

transposta = [[] for _ in range(num_colunas)]

print(transposta)


for i in range(num_linha):
    for j in range(num_colunas):
        transposta[j].append(matriz_progomal[i][j])

for linha in transposta:
    print(linha)
