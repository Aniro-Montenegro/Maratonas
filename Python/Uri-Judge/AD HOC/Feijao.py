"""
SUBMISSÃO # 26165041
PROBLEMA:
2791 - Feijão
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.9 (Python 3.9.4) [+1s] {beta}
TEMPO:
0.275s
TAMANHO:
112 Bytes
MEMÓRIA:
-
SUBMISSÃO:
06/02/2022 15:51:40
"""

dados = input()
lista = dados.split(" ")

for n in range(4):
    if lista[n] == '1':
        print(n + 1)

"""
SUBMISSÃO # 26165128
PROBLEMA:
2791 - Feijão
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.145s
TAMANHO:
0 Bytes
MEMÓRIA:
-
SUBMISSÃO:
06/02/2022 15:58:15
"""
dados = input()
dados = dados.replace(" ", "")
print(dados.rfind("1") + 1)


