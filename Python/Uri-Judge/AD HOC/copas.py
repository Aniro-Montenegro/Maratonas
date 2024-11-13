n = int(input())
m = int(input())
lista=[]
for _ in range(m):
    a=int(input())
    if a !=lista[0]:
        lista.insert(0,a)

print(n-(len(lista)))