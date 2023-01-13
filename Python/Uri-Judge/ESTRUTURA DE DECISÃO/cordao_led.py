dados=input().split(" ")
N=int(dados[0])
L=int(dados[1])
lista=[]
x=0
i=1
for _ in range(N):
    lista.insert(x,i)
    x=x+1
    lista.insert(x,-1)
    i=i+1
    x=x+1
d=len(lista)
lista[d-1]=0
for _ in range(L):
    xy=input().split(" ")
    a=int(xy[0])
    b=int(xy[1])
    for i in range(len(lista)):
        if lista[i]==-1:
            if lista[i-1]>=a and lista[i+1]<=b:
                lista[i]=0
        if i>b:
            break
boleano=True
k=0

for a in range(len(lista)):
    if lista[k]==-1:
        boleano=False
    k=k+1
if boleano==False:
    print('INCOMPLETO')
else:
    print('COMPLETO')
    
    