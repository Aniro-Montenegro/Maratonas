'''
SUBMISSÃO # 27667356PROBLEMA:
3047 - A idade de Dona Mônica
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.192s
TAMANHO:151 Bytes
MEMÓRIA:-
SUBMISSÃO:30/04/2022 21:24:44

1044	27667356	AniroMontenegro	Python 3.8	0.192	01/05/2022 00:24:44
'''
mae = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = mae - (filho1 + filho2)
lista = [filho1, filho2, filho3]
print(max(lista))
