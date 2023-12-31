dados=input().split(' ')
a=int(dados[0])
b=int(dados[1])
x=1
if a<0:
    a=a*-1
    x=-1
if b<0:
    b=b*-1
    x=-1

#a = b × q + r
q=a-1
r=1
while True:
    print(b*q+r==a)
    if b*q+r==a:
        print(q*x,r)
        break
    q=q-1
    if q==r:
        r=r+1
        q=a-1