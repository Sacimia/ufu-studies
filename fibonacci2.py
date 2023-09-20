print("-"*50)
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(F"O VALOR DE ENESIMO TERMO DA FUNÇAO DE FIBONACCI É {termo}")

    #print("O VALOR DE ENESIMO TERMO DA FUNÇAO DE FIBONACCI É", termo)
print("-"*50)
