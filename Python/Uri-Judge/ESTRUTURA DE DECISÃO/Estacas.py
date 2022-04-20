while True:
    try:
        dados = input().split(" ")
        if dados[0] == dados[1]:
            print(4)
        elif (int(dados[0]) % 2 == 0 and int(dados[1]) % 2 != 0) or (
                int(dados[0]) % 2 != 0 and int(dados[1]) % 2 == 0):
            valor = (int(dados[0]) * 2) + (int(dados[1]) * 2)
            print(valor)
        else:
            valor = int(((int(dados[0]) * 2) + (int(dados[1]) * 2))/2)
            print(valor)

    except EOFError as e:
        break
