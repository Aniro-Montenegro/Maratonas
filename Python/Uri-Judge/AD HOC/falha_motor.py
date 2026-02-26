a = int(input())
lista = [int(x) for x in input().split()]

i = 0
b = 0
cont = 0
variavel = 0

for d in lista:
    if i == 0:
        b = d
    else:
        if d < b and cont == 0:
            cont = 1
            variavel = i + 1
    b = d
    i += 1
print(variavel)
