"""
SUBMISSÃO # 26746861
PROBLEMA:3004 - Envelopes
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.299s
TAMANHO:286 Bytes
MEMÓRIA:-
SUBMISSÃO:16/03/2022 00:03:56

99	26746861	Aniro Montenegro	Python 3.8	0.299	16/03/2022 03:03:56

2881	Aniro Montenegro	FATEC-SJC	790,03	↥28
"""


n = int(input())

for _ in range(n):
    dados = input().split()
    if int(dados[0]) < int(dados[2]) and int(dados[1]) < int(dados[3]):
        print('S')
    elif int(dados[0]) < int(dados[3]) and int(dados[1]) < int(dados[2]):
        print('S')
    else:
        print('N')

