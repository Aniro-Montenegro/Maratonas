"""
SUBMISSÃO # 26733976
PROBLEMA:3040 - A Árvore de Natal
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.183s
TAMANHO:217 Bytes
MEMÓRIA:-
SUBMISSÃO:15/03/2022 12:47:44

389	26733976	Aniro Montenegro	Python 3.8	0.183	15/03/2022 15:44:31

2931   Aniro Montenegro	FATEC-SJC	782,86	↥14
"""

n = int(input())

for _ in range(n):
    dados = input().split(" ")
    if (200 <= int(dados[0]) <= 300) and int(dados[1]) >= 50 and int(dados[2]) >= 150:
        print('Sim')
    else:
        print('Nao')
