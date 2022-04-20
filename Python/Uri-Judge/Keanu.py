"""
SUBMISSÃO # 26485266
PROBLEMA:
3342 - Keanu
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.035s
TAMANHO:189 Bytes
MEMÓRIA:
-
SUBMISSÃO:
27/02/2022 20:39:10
"""

"""
52	26485266	Aniro Montenegro	Python 3.8	0.035	27/02/2022 23:39:10
"""

"""
n=int(input())
n=n*n
brancas=0
pretas=0

for i in range(n):
    if i%2==0:
        brancas+=1
    else:
        pretas+=1
print(f'{brancas} casas brancas e {pretas} casas pretas')
"""


"""
PROBLEMA:
3342 - Keanu
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.096s
TAMANHO:
302 Bytes
MEMÓRIA:
-
SUBMISSÃO:
27/02/2022 20:49:19

"""

n = int(input())
z = n * n
brancas = 0
pretas = 0

if n % 2 == 0:
    brancas = n * (n // 2)
    pretas = brancas
else:
    for i in range(z):
        if i % 2 == 0:
            brancas += 1
        else:
            pretas += 1
print(f'{brancas} casas brancas e {pretas} casas pretas')
