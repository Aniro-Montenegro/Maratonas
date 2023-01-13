i=int(input())
for _ in range(i):

    dados=input().split(" ")
    a=int(dados[0])
    b=int(dados[1])
    total=0
    while a>b :
        a=a-b
        total=total+1
    print(total+a)
    