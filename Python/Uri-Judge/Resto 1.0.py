"""
SUBMISSÃO # 26182880
PROBLEMA:
3091 - Resto 1.0
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.4 (Python 3.4.3) [+1s]
TEMPO:
0.025s
TAMANHO:
259 Bytes
MEMÓRIA:
-
SUBMISSÃO:
08/02/2022 00:14:02


RANKING    SUBMISSÃO     USUÁRIO	        LINGUAGEM        TEMPO          DATA DA SUBMISSÃO
294	        26182880	Aniro Montenegro	Python 3	      0.025	         07/02/2022 14:20:48

"""


def calculaResto(a, b):
    resto = a % b
    if resto == 0:
        resto = a // b
    if resto > b:
        calculaResto(a, resto)
    else:
        print(resto)


n = int(input())
m = int(input())

if n < m:
    print(n)
else:
    calculaResto(n, m)
