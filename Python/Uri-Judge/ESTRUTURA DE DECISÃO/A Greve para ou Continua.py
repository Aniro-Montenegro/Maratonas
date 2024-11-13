n=int(input())
g=0
v=0
for i in range(n):
    x=input().split()
    if x[0]=="G":
        g+=int(x[1])
    else:
        v+=int(x[1])
print("NAO VAI TER CORTE, VAI TER LUTA!" if g>v else "A greve vai parar.")
