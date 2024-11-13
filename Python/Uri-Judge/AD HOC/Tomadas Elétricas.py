n = int(input())

for _ in range(n):
    dados = [int(x) for x in input().split()]
    soma = 0
    for x in range(1, dados[0]+1):
        print(dados[x])
        soma += soma + dados[x] - 1
        print('soma',soma)
    soma += 1
    print(soma)
