comprimento = 0
distancia = 0
custo_quilometro = 0
valor_pedagio = 0
custo_total = 0

primeira_linha = input().split(" ")
comprimento = int(primeira_linha[0])
distancia = int(primeira_linha[1])
segunda_linha = input().split(" ")
custo_quilometro = int(segunda_linha[0])
valor_pedagio = int(segunda_linha[1])
indice = 1

for i in range(1, comprimento + 1):
    custo_total += custo_quilometro
    if indice == distancia:
        custo_total += valor_pedagio
        indice = 1
    indice += 1
print(custo_total)
