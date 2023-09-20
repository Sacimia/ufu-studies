
ntermos = int(input("Quantos termos? "))

n1, n2 = 0, 1
count = 0

if ntermos <= 0:
   print("por favor uma integer positivo")
elif ntermos == 1:
   print("",ntermos,":")
   print(n1)
else:
   print("Sequencia Fibonacci:")
   while count < ntermos:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
