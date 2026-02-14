n=int(input())
lista=[]

for i in range(n):
    if(i==0 or i==1):
        lista.append(1)
    else:
        lista.append(lista[i-1]+lista[i-2])
lista2=lista[::-1]
resultado = ' '.join(map(str, lista2))
print(resultado)
    
   