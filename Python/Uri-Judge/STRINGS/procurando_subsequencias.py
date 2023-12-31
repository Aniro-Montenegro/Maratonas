caso=1
while True:
    try:
        a=input()
        b=input()
        i=0
        l=0
        z=0
        
        r=len(b)-len(a)+1
        for _ in range(r):
            if a in b[i:i+len(a)]:
                l=l+1
                z=i
            i=i+1
        if l>0:
            print(f"Caso #{caso}:")
            print(f"Qtd.Subsequencias: {l}")
            print(f"Pos: {z+1}")
            print()
        else:
            print(f"Caso #{caso}:")
            print(f"Nao existe subsequencia")
            print()
            
        caso=caso+1
        
                
    except:
        break