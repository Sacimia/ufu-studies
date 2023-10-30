pessoas = {"Nome":"Marcos", "Idade":19, "Peso":100, "Sexo": "M"}

for k in pessoas.keys():
    print("Chavs = ", k)
for k in pessoas.values():
    print("Valor = ", k)
for k, v in pessoas.items():
    print(f"{k}\t=\t{v}")
