"""
SUBMISSÃO # 26165377
PROBLEMA:
3037 - Jogando Dardos Por Distância
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.4 (Python 3.4.3) [+1s]
TEMPO:
0.116s
TAMANHO:
366 Bytes
MEMÓRIA:
-
SUBMISSÃO:
06/02/2022 16:20:25


"""

n = int(input())
for _ in range(n):
    joao = 0
    maria = 0
    for x in range(3):
        dados = input().split(" ")
        joao += (int(dados[0]) * int(dados[1]))
    for x in range(3):
        dados = input().split(" ")
        maria += (int(dados[0]) * int(dados[1]))
    if maria > joao:
        print('MARIA')
    else:
        print('JOAO')
