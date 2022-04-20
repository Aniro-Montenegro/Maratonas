# n=int(input())
# lista=[]
# palavra=""
# menor=0
# for s in range(n):
#     t=tuple(input().split())
#     lista.append(t)
# i=0
#
# while len(palavra)<n:
#     if int(lista[i][0])==menor:
#         palavra+=lista[i][1]
#
#         menor=int(lista[i][2])
#         lista.pop(i)
#
#     i+=1
#     if i>=len(lista):
#         i=0
#
# print(palavra)
#
# '''
# 4
# 5 A 1
# 0 T 7
# 3 M 5
# 7 E 3
#
#
# TEMA
# '''


class Objeto:
    def __init__(self):
        self.numero_anterior = '0'
        self.letra = ""
        self.numero_posterior = '0'


n = int(input())
lista = []
palavra = ""
menor = 0
for s in range(n):
    t = tuple(input().split())
    objeto = Objeto()
    objeto.numero_anterior, objeto.letra, objeto.numero_posterior = t
    lista.append(objeto)
indice = '0'
while len(palavra) < n:
    i = 0
    while i < len(lista):
        if lista[i].numero_anterior == indice:
            palavra = palavra + lista[i].letra
            indice = lista[i].numero_posterior
            lista.pop(i)
        i += 1
print(palavra)
