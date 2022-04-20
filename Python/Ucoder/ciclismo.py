"""
Detalhes da submissão
Problema: Ciclismo
Resultado: Accepted
Tempo: 0,3828
Submissão: 13/02/2022 02:39:06



	    PROBLEMA	USUÁRIO	            LINGUAGEM	TEMPO	RANKING
31405	Ciclismo	Aniro Montenegro	Python 3.4	0,3828	#1

"""

nome1 = input()
v1 = float(input())
nome2 = input()
v2 = float(input())
nome3 = input()
v3 = float(input())

m = 75000
t = (v1 * 1000) // 60
hora = 0
minuto = 0

while True:
    m = m - t
    if m < 0:
        break
    else:

        minuto = minuto + 1
        if minuto >= 60:
            hora += 1
            minuto = 0
vr = str(hora) + "h" + str(minuto)
tupla1 = (nome1, vr)

m = 75000
t = (v2 * 1000) // 60
hora = 0
minuto = 0

while True:
    m = m - t
    if m < 0:
        break
    else:

        minuto = minuto + 1
        if minuto >= 60:
            hora += 1
            minuto = 0
vr = str(hora) + "h" + str(minuto)
tupla2 = (nome2, vr)

m = 75000
t = (v3 * 1000) // 60
hora = 0
minuto = 0

while True:
    m = m - t
    if m < 0:
        break
    else:
        minuto = minuto + 1
        if minuto >= 60:
            hora += 1
            minuto = 0
vr = str(hora) + "h" + str(minuto)
tupla3 = (nome3, vr)

lista = [tupla1, tupla2, tupla3]

lista.sort(key=lambda x: x[1])

for x in lista:
    print(x[0] + " " + x[1])
