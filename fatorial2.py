n=int(input("Entre com N: "))
p=1
i=1
while True:
##while i<=n
    if(i>=n):
        break
    ##else:
    ##    continue
    p*=i
    i+=1
    print(f"O fatorial de {n} = {p}")
