"""
Resultado: Accepted
Tempo: 1,1564
Submissão: 14/02/2022 16:21:02




"""

# guarda = 0
# dados = input()
# dados = dados.split()
# ladrao = int(dados[0])
# velocidade_ladrao = int(dados[1])
# velocidade_guarda = int(dados[2])
# pegou="N"
# diferenca=abs(velocidade_guarda-velocidade_ladrao)
# if diferenca<ladrao:
#     print('N')
# else:
#     print('S')


while True:
    try:
        guarda = 0
        dados = input()
        dados = dados.split()
        ladrao = int(dados[0])
        velocidade_ladrao = int(dados[1])
        velocidade_guarda = int(dados[2])
        diferenca = abs(velocidade_guarda - velocidade_ladrao)
        if diferenca < ladrao:
            print('N')
        else:
            print('S')


    except EOFError as e:
        break