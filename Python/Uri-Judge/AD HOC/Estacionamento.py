dados = input().split(" ")
n = int(dados[0])
k = int(dados[1])
lista = []
resultado = 'Sim'

for _ in range(n):
    carro = input().split(" ")
    carro[0] = int(carro[0])
    carro[1] = int(carro[1])
    if len(lista) >= 0:
        lista.append(carro)
    else:

        lista[0][1] = lista[0][1] - carro[0]
        if lista[0][1] <=0:
            lista.remove(lista[0])
            lista.append(carro)
        else:
            if carro[1] >= lista[0][1]:
                lista.append(carro)
            else:
                lista[0][1]-=carro[1]


print(lista)
