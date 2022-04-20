"""
SUBMISSÃO # 26852843
PROBLEMA:2543 - Jogatina UFPR
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.417s
TAMANHO:349 Bytes
MEMÓRIA:-
SUBMISSÃO:20/03/2022 21:22:10

429	26852843	Aniro Montenegro	Python 3.8	0.417	21/03/2022 00:22:10
2841	Aniro Montenegro	FATEC-SJC	797,75	↥13
"""

while True:
    try:
        dados1 = input().split()
        n = int(dados1[0])
        contador = 0
        game = dados1[1]
        for _ in range(n):
            dado = input().split()
            if dado[0] == game and dado[1] == '0':
                contador += 1
        print(contador)

    except EOFError as e:
        break
