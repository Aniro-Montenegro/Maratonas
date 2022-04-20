"""
SUBMISSÃO # 26283068
PROBLEMA:
1581 - Conversa Internacional
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.043s
TAMANHO:
298 Bytes
MEMÓRIA:
-
SUBMISSÃO:
15/02/2022 00:29:29


748	26283068	Aniro Montenegro	Python 3.8	0.043	15/02/2022 03:29:29
"""

n = int(input())

for _ in range(n):
    numero_pessoas = int(input())
    lista = []
    for _ in range(numero_pessoas):
        palavra = input()
        if palavra not in lista:
            lista.append(palavra)

    if len(lista) == 1:
        print(lista[0])
    else:
        print('ingles')





"""
SUBMISSÃO # 26283146
PROBLEMA:
1581 - Conversa Internacional
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.268s
TAMANHO:
273 Bytes
MEMÓRIA:
-
SUBMISSÃO:
15/02/2022 00:42:58

"""
n = int(input())

for _ in range(n):
    numero_pessoas = int(input())
    lista = []
    for _ in range(numero_pessoas):
        palavra = input()
        lista.append(palavra)
    if (len(set(lista)))==1:
        print(lista[0])
    else:
        print('ingles')