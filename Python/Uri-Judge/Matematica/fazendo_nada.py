while True:
    dados = [int(x) for x in input().split()]
    if dados[0] == -1 and dados[1] == -1:
        break
    lista = [int(x) for x in input().split()]
    capitulos = 0
    tamanho = len(lista)
    for x in lista:
        capitulos += x * tamanho
        tamanho -= 1
    print(capitulos * dados[1])
