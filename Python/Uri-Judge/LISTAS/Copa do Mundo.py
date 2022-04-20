"""
SUBMISSÃO # 26486758
PROBLEMA:2376 - Copa do Mundo
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.087s
TAMANHO:881 Bytes
MEMÓRIA:-
SUBMISSÃO:27/02/2022 23:43:18

110	26486758	Aniro Montenegro	Python 3.8	0.087	28/02/2022 02:31:29

"""

lista_times = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
indice = 0

for n in range(8):
    jogo = input().split(" ")
    if int(jogo[0]) > int(jogo[1]):
        lista_times.pop(indice + 1)
    else:
        lista_times.pop(indice)
    indice += 1

indice = 0
for n in range(4):
    jogo = input().split(" ")
    if int(jogo[0]) > int(jogo[1]):
        lista_times.pop(indice + 1)
    else:
        lista_times.pop(indice)
    indice += 1
indice = 0
for n in range(2):
    jogo = input().split(" ")
    if int(jogo[0]) > int(jogo[1]):
        lista_times.pop(indice + 1)
    else:
        lista_times.pop(indice)
    indice += 1
indice = 0
for n in range(1):
    jogo = input().split(" ")
    if int(jogo[0]) > int(jogo[1]):
        lista_times.pop(indice + 1)
    else:
        lista_times.pop(indice)
    indice += 1
print(lista_times[0])
