while True:
    quantidade=0
    palavra = input()
    if palavra == ".":
        break
    else:
        lista = palavra.split()
        dicionario = {}
        for pal in lista:
            if len(pal) > 2:
                dicionario[pal]=pal[0:1] + "."
                quantidade+=1
            else:
                dicionario[pal]=pal
    sorted(dicionario)
    print(quantidade)
