"""
SUBMISSÃO # 27256242
PROBLEMA:2510 - Batmain
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.111s
TAMANHO:147 Bytes
MEMÓRIA:-
SUBMISSÃO:08/04/2022 09:03:10

784	27256242	Aniro Montenegro	Python 3.8	0.111	08/04/2022 12:03:10

"""

n=int(input())

for i in range(n):
    palavra=input()
    if(palavra.islower()=='batmain'):
        print('N')
    else:
        print('Y')