"""
SUBMISSÃO # 26172524
PROBLEMA:
3147 - A Batalha dos Cinco Exércitos
RESPOSTA:Accepted
LINGUAGEM:Python 3.4 (Python 3.4.3) [+1s]
TEMPO:0.014s
TAMANHO:236 Bytes
MEMÓRIA:-
SUBMISSÃO:07/02/2022 10:39:32

RANKING    SUBMISSÃO     USUÁRIO	        LINGUAGEM        TEMPO          DATA DA SUBMISSÃO
94	       26172524	     Aniro Montenegro	Python 3	     0.014	       07/02/2022 13:39:32
"""


numeros = input()
lista = numeros.split(" ")
a = int(lista[0]) + int(lista[1]) + int(lista[2]) + int(lista[5])
b = int(lista[3]) + int(lista[4])
if a > b:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')
