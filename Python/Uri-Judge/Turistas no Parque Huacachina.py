"""
SUBMISSÃO # 26979611
PROBLEMA:2708 - Turistas no Parque Huacachina
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.187s
TAMANHO:353 Bytes
MEMÓRIA:-
SUBMISSÃO:25/03/2022 19:12:46

426	26979611	Aniro Montenegro	Python 3.8	0.187	25/03/2022 22:12:46

2834	Aniro Montenegro	FATEC-SJC	799,40	↥8

"""

jipes = 0
turistas = 0
while True:
    dados = input()

    if dados == 'ABEND':
        break
    else:
        lista = dados.split(" ")
        if lista[0] == 'SALIDA':
            jipes += 1
            turistas += int(lista[1])
        else:
            jipes -= 1
            turistas -= int(lista[1])
print(turistas)
print(jipes)
