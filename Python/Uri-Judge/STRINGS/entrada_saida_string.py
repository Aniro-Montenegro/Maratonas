palavra1 = input()
palavra2 = input()
palavra3 = input()

pal1 = ""
pal2 = ""
pal3 = ""

if len(palavra1) > 10:
    pal1 = palavra1[0:10]
else:
    pal1 = palavra1

if len(palavra2) > 10:
    pal2 = palavra2[0:10]
else:
    pal2 = palavra2

if len(palavra3) > 10:
    pal3 = palavra3[0:10]
else:
    pal3 = palavra3
print(palavra1 + palavra2 + palavra3)
print(palavra2 + palavra3 + palavra1)
print(palavra3 + palavra1 + palavra2)
print(pal1 + pal2 + pal3)
