"""

SUBMISSÃO # 26255224
PROBLEMA:
1234 - Sentença Dançante
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.434s
TAMANHO:
461 Bytes
MEMÓRIA:
-
SUBMISSÃO:
13/02/2022 02:56:29

1082	26255224	Aniro Montenegro	Python 3.8	0.434	13/02/2022 05:31:03


RANKING		USUÁRIO	UNIVERSIDADE	PONTOS
3154         Aniro Montenegro	    FATEC-SJC	745,96	↥45
"""

while True:
    try:
        palavra = input()
        z = 1
        lista = []
        for a in palavra:
            if z % 2 == 0 and a != " ":
                lista.append(a.lower())
            elif a != " ":
                lista.append(a.upper())
            else:
                lista.append(a)
            if a != " ":
                z += 1
        p = "".join(lista)
        print(p)

    except EOFError as e:
        break


