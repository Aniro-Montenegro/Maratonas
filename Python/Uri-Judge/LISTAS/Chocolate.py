"""
SUBMISSÃO # 27773836
PROBLEMA:2328 - Chocolate
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.096s
TAMANHO:145 Bytes
MEMÓRIA:-
SUBMISSÃO:05/05/2022 23:35:41

2791	AniroMontenegro	FATEC-SJC	811,47	↥14
"""

n = int(input())
lista = input()
lista2 = lista.split()

soma = 0
for v in lista2:
    x = int(v)
    soma = soma + (x - 1)
print(soma)
