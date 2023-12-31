while True:
    x=input().split(" ")
    a=x[0]
    k=x[1]
    if a!="0" and k!="0":
        b=list(k)    
        nova_lista = [elemento for elemento in b if elemento != a]

        f="".join(nova_lista)
        if len(nova_lista)==0:
            print(0)
        else:
            print(int(f))
    else:
        break
