n=int(input())

for a in range(n):
    palavra=list(input())
    lista=[]
    for p in palavra:       
        codigo_ascii = ord(p)
        if((codigo_ascii>=65 and codigo_ascii<=90) or(codigo_ascii>=97 and codigo_ascii<=122)):
            codigo_ascii+=3
            lista.append(chr(codigo_ascii))
        else:
            lista.append(p)
        
    lista.reverse()
    lista_invertida=lista
    tamanho=len(lista_invertida)
    metade = tamanho // 2
    while(metade<tamanho):
        codigo_ascii = ord(lista_invertida[metade])
        codigo_ascii-=1
        lista_invertida[metade]=chr(codigo_ascii)
        metade+=1
    final="".join(lista_invertida)
    print(final)
        
        

