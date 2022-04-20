"""
SUBMISSÃO # 26606597
PROBLEMA:1515 - Hello Galaxy
RESPOSTA:Accepted
LINGUAGEM:Python 3.4 (Python 3.4.3) [+1s]
TEMPO:0.094s
TAMANHO:397 Bytes
MEMÓRIA:-
SUBMISSÃO:08/03/2022 01:22:07

245	26606597	Aniro Montenegro	Python 3	0.094	08/03/2022 04:22:07
"""

while True:
    n = int(input())
    if n == 0:
        break
    lista = []

    dicionarios = {}

    for _ in range(n):
        palavra = tuple(input().split(" "))
        dicionarios[palavra[0]] = int(palavra[1]) - int(palavra[2])

    for i in sorted(dicionarios, key=dicionarios.get):
        lista.append(i)
        if len(lista) > 0:
            break
    print(lista[0])
