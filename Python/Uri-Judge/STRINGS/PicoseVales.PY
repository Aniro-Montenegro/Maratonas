a = int(input())
listas = input().split(" ")
lista = list(map(int, listas))

tamanho = len(lista)
padrao = []
v = 1  

for i in range(tamanho - 1):
    if lista[i] < lista[i + 1]:
        padrao.append(1)
    elif lista[i] > lista[i + 1]:
        padrao.append(0)
    else:
        v = 0
        break

for i in range(len(padrao) - 1):
    if padrao[i] == padrao[i + 1]:
        v = 0
        break

print(v)
