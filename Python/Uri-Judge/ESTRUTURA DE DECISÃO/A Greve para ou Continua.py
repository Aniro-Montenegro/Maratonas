# Problema:# 2982 - A Greve para ou Continua?
# Resposta:# Accepted
# Linguagem:# Python 3.9 AI (Python 3.9.4, V.1.0) [+1s] {beta}
# Tempo:# 0.204s
# Tamanho:# 237 Bytes
# Submissão:# 12/11/2024 23:09:21

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
