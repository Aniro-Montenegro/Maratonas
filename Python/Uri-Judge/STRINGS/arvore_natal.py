while True:
    try:
        n=int(input())
        i=1
        lista=['*'] * n
        lista2=['*'] * n
        metade = int(n/2)+1
        direita = metade
        esquerda = metade
        while direita < n and esquerda > 0:
            for j in range(n):
                if j >= esquerda and j <= direita:
                    lista[j] = '*'
                else:
                    lista[j] = " "
            print(''.join(lista).rstrip())
            direita += 1
            esquerda -= 1
        final=" "*(metade)
        final+="*"
        
        final2=" "*(metade-1)
        final2+="***"
        
        print(" "+"".join(lista2).rstrip())
        print(final.rstrip())
        print(final2.rstrip())
        print()
        
       
    except EOFError as e:
        break

