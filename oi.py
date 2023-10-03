n = 1000
for i in range(1,n+1):
  print (i, " oi")
      if(i%2)==0:
          print(i, "eh par")
      else:
          print(i, "eh impar")
# Inicialize uma lista vazia para armazenar os números
numeros = []

# Use um loop while True para permitir que o usuário insira os números
while True:
    entrada = input("Digite um número (ou 's' para sair): ")
    
    if entrada.lower() == 's':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")

# Verifique se a lista não está vazia
if numeros:
    # Inicialize as variáveis para armazenar o número menor e maior
    numero_menor = numeros[0]
    numero_maior = numeros[0]

    # Use um loop para encontrar o número menor e o número maior
    for numero in numeros:
        if numero < numero_menor:
            numero_menor = numero
        if numero > numero_maior:
            numero_maior = numero

    # Imprima o número menor e o número maior
    print("O número menor na lista é:", numero_menor)
    print("O número maior na lista é:", numero_maior)
else:
    print("A lista está vazia.")
