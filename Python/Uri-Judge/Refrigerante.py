dados=input().split(" ")
a=int(dados[0])
b=int(dados[1])
c=int(dados[2])
totalCascos=a+b
refrigerantes=totalCascos//c
resto=totalCascos%2
totalCascos=refrigerantes+resto
while(totalCascos>=c):
    refrigerantes+=totalCascos//c
    resto=totalCascos%2
    totalCascos=totalCascos//c+resto
print(refrigerantes)