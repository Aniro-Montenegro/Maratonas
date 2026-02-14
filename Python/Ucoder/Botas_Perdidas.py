n=int(input())
lista=[]
listaaux=[]
for a in range(n):
    entrada=input()
    partes = entrada.split()
    tupla=(partes[0],partes[1])
    lista.append(tupla)
indice=1
contador=0
while len(lista)>0:
    if lista[0][0] == lista[indice][0] and ((lista[0][1]=='E' and lista[indice][1]=='D') or(lista[0][1]=='D' and lista[indice][1]=='E') ):
        lista.pop(indice)
        lista.pop(0)
        indice=0
        contador+=1
    indice+=1
    if indice== len(lista):
        lista.pop(0)
        indice=0
       
 


    
print(contador)

# Detalhes da submissão
# Problema: Botas Perdidas
# Resultado: Accepted
# Tempo: 0,9275
# Submissão: 04/04/2025 13:48:49

#teste
# 30
# 36 E
# 36 D
# 37 E
# 37 D
# 38 E
# 38 D
# 39 E
# 39 D
# 40 E
# 40 D
# 41 E
# 41 D
# 42 E
# 42 D
# 43 E
# 43 D
# 44 E
# 44 D
# 45 E
# 45 D
# 36 E
# 37 E
# 38 E
# 39 E
# 40 E
# 41 E
# 42 E
# 43 E
# 44 E
# 45 E

#teste 2 10 pares
# 30
# 38 E  
# 40 D  
# 36 E  
# 36 D  
# 42 E  
# 39 D  
# 37 E  
# 45 D  
# 41 E  
# 44 D  
# 43 E  
# 37 D  
# 38 D  
# 39 E  
# 40 E  
# 41 D  
# 42 D  
# 43 D  
# 44 E  
# 45 E  
# 36 E  
# 37 E  
# 38 E  
# 39 E  
# 40 E  
# 41 E  
# 42 E  
# 43 E  
# 44 E  
# 45 E

#teste 7 pares
# 60
# 36 E  
# 36 D  
# 37 E  
# 37 D  
# 38 E  
# 38 D  
# 39 E  
# 39 D  
# 40 E  
# 40 D  
# 41 E  
# 41 D  
# 42 E  
# 42 D  
# 36 E  
# 37 E  
# 38 E  
# 39 E  
# 40 E  
# 41 E  
# 42 E  
# 43 E  
# 44 E  
# 45 E  
# 43 D  
# 44 D  
# 45 D  
# 43 E  
# 44 E  
# 45 E
# 36 E  
# 36 D  
# 37 E  
# 37 D  
# 38 E  
# 38 D  
# 39 E  
# 39 D  
# 40 E  
# 40 D  
# 41 E  
# 41 D  
# 42 E  
# 42 D  
# 36 E  
# 37 E  
# 38 E  
# 39 E  
# 40 E  
# 41 E  
# 42 E  
# 43 E  
# 44 E  
# 45 E  
# 43 D  
# 44 D  
# 45 D  
# 43 E  
# 44 E  
# 45 E