numero = float(input())
pi = 3.14
circunferencia = 2 * pi * numero
lista=str(circunferencia).split(".")
primeiro=lista[0]
segundo=lista[1][0:2]
print(primeiro+"."+segundo)

