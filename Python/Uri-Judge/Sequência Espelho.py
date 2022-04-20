"""
SUBMISSÃO # 26255072
PROBLEMA:
2157 - Sequência Espelho
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.524s
TAMANHO:
390 Bytes
MEMÓRIA:
-
SUBMISSÃO:
13/02/2022 02:17:31

788	26255072	Aniro Montenegro	Python 3	0.524	13/02/2022 05:15:51

"""

n = int(input())
for _ in range(n):
    dados = input()
    dados = dados.split(" ")
    v1 = int(dados[0])
    v2 = int(dados[1])
    d = abs(v1 - v2)
    d = (d + 1)
    for _ in range(d):
        print(v1, end="")
        v1 = v1 + 1
    for _ in range(d):
        s = str(v2)
        s = s[::-1]
        print(s, end="")
        v2 -= 1
    print()
