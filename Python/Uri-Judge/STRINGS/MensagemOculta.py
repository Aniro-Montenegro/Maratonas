# PROBLEMA:1272 - Mensagem Oculta
# RESPOSTA:Accepted
# LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
# TEMPO:0.237s
# SUBMISSÃO:31/12/2023 11:04:22

n=int(input())
for i in range(n):
    palavra=input().split(" ")
    novaPalavra=""
    for p in palavra:
        if p!=" " and p!="":
            novaPalavra+=p[0]
    print(novaPalavra)