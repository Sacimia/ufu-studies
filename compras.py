produto = list()
n = int(input("entre com qtd de produtos: "))
for i in range(n):
    produto.append(str(input("eNTRE COM NOME DO PRODUTO: ")))
    produto.append(int(input("entre com o preço: ")))

print("-"*61)
for i in range(2*n):
    if i %2 == 0:
        print(f"{produto[i]:^30}:", end="")
    else:
        print(f'{f"R${produto[i]:.2f}":^30}')
print("-"*61)
