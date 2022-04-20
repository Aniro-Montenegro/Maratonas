"""
SUBMISSÃO # 26183081
PROBLEMA:
1098 - Sequencia IJ 4
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.307s
TAMANHO:
797 Bytes
MEMÓRIA:
-
SUBMISSÃO:
08/02/2022 00:42:59


"""

i = 0
j = 1

for n in range(3):
    print(f'I={i} J={j}')
    j += 1
i = 0.2
j = 1.2

for n in range(3):
    print(f'I={i} J={j}')
    j += 1
i = 0.4
j = 1.4
for n in range(3):
    print(f'I={i} J={j}')
    j += 1

i = 0.6
j = 1.6
for n in range(3):
    print(f'I={i} J={j}')
    j += 1

i = 0.8
j = 1.8
for n in range(3):
    print(f'I={i} J={j}')
    j += 1

i = 1
j = 2
for n in range(3):
    print(f'I={i} J={j}')
    j += 1

i = 1.2
j = 2.2

for n in range(3):
    print(f'I={i} J={j}')
    j += 1

i = 1.4
j = 2.4

for n in range(3):
    print(f'I={i} J={j}')
    j += 1

i = 1.6
j = 2.6

for n in range(3):
    print(f'I={i} J={j}')
    j += 1
i = 1.8
j = 2.8

for n in range(3):
    print(f'I={i} J={j}')
    j += 1
i = 2
j = 3

for n in range(3):
    print(f'I={i} J={j}')
    j += 1

"""

SUBMISSÃO # 26183220
PROBLEMA:
1098 - Sequencia IJ 4
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.212s
TAMANHO:
449 Bytes
MEMÓRIA:
-
SUBMISSÃO:
08/02/2022 01:12:41


RANKING    SUBMISSÃO     USUÁRIO	        LINGUAGEM        TEMPO          DATA DA SUBMISSÃO
4477	     26183220	Aniro Montenegro	  Python 3	      0.212       	08/02/2022 03:37:26

"""
i = 0
j = 1
cont = 0
while j <= 5:

    i = round(i, 1)
    j = round(j, 1)
    if i in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]:
        i = int(i)
    if j in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]:
        j = int(j)
    print(f'I={i} J={j}')
    cont += 1
    if cont == 3:
        i = round((i + 0.2), 1)

        if j>=5:
            break
        else:
            j = 1 + round(i, 1)

        cont = 0
    else:
        j += 1






