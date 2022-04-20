import datetime

dia_inicial = input()
dia_inicial_int = int(dia_inicial.split()[1])
hora_inicial = input()
hora_inicial_lista = hora_inicial.split(":")

dia_final = input()
dia_final_int = int(dia_final.split()[1])
hora_final = input()
hora_final_lista = hora_final.split(":")

data1 = datetime.datetime(year=2000, month=1, day=dia_inicial_int, hour=int(hora_inicial_lista[0]),
                          minute=int(hora_inicial_lista[1]), second=int(hora_inicial_lista[2]))
data2 = datetime.datetime(year=2000, month=1, day=dia_final_int, hour=int(hora_final_lista[0]),
                          minute=int(hora_final_lista[1]), second=int(hora_final_lista[2]))

diferenca = data2 - data1

lista = str(diferenca).split()

lista_hora = lista[len(lista) - 1].split(":")
dia = 0
if len(lista) > 2:
    dia = int(lista[0])
hora = int(lista_hora[0])
minutos = int(lista_hora[1])
segundos = int(lista_hora[2])

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')


'''
RANKING
4783	26073310	Aniro Montenegro	Python 3.8	0.185	29/01/2022 17:02:09

PROBLEMA:
1061 - Tempo de um Evento
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.185s
TAMANHO:
1,02 KB
MEMÓRIA:
-
SUBMISSÃO:
29/01/2022 14:13:31
'''