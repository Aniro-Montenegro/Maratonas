"""

Problema: Atletismo
Resultado: Accepted
Tempo: 0,2409
Submissão: 08/02/2022 03:49:30


  #      PROBLEMA	USUÁRIO	            LINGUAGEM	TEMPO	RANKING
31400	Atletismo	Aniro Montenegro	Python 3.4	0,2409	#1

"""

nome1 = input()
dados1 = input()
nome2 = input()
dados2 = input()
nome3 = input()
dados3 = input()
lista1 = dados1.split(" ")
lista2 = dados2.split(" ")
lista3 = dados3.split(" ")
lista1.sort()
lista1.reverse()
tupla1 = (nome1, lista1[0])
lista2.sort()
lista2.reverse()
tupla2 = (nome2, lista2[0])
lista3.sort()
lista3.reverse()
tupla3 = (nome3, lista3[0])
listaF = [tupla1, tupla2, tupla3]
listaF.sort(key=lambda x: x[1])
listaF.reverse()
for x in listaF:
    print(x[0] + " " + x[1])


