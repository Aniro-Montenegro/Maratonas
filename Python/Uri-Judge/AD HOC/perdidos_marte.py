n = int(input())
lista_string = input()
lista = lista_string.split(" ")
frase = ""

for c in lista:
    frase = frase + chr(int(c, 16))

print(frase)
