n = int(input())
for _ in range(n):
    palavra = input()
    palavra=palavra+'x'
    a = ''
    total = 0
    tamanho = len(palavra)
    i = 0
    while i < tamanho:
        if 48 <= ord(palavra[i]) <= 57:
            a = a + palavra[i]
            x = i + 1
            while x < tamanho:
                if 48 <= ord(palavra[x]) <= 57:
                    a = a + palavra[x]
                    x += 1
                else:
                    i = x-1
                    total = total + int(a)
                    a = ''
                    break

        i += 1
    print(total)



"""
RANKING
486     	26127271	Aniro Montenegro	Python 3	0.192	03/02/2022 05:03:13


SUBMISSÃO # 26127271
PROBLEMA:
2694 - Problema com a Calculadora
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.4 (Python 3.4.3) [+1s]
TEMPO:
0.192s
TAMANHO:
610 Bytes
MEMÓRIA:
-
SUBMISSÃO:
03/02/2022 02:03:13

"""



"""

Joãozinho tem que ajudar seu pai. Um relatório específico com alguns números está saindo com caracteres indesejáveis no 
meio. 
A ideia é apenas somar os 3 valores que aparecem em cada linha sempre na mesma posição, ignorando as letras e 
apresentar esta soma. Não existem espaços em branco na linha.

Entrada
A primeira linha de entrada contém um inteiro N (N < 100000). Seguem N linhas com exatos 14 caracteres que devem ser 
lidas e delas extraídos e somados os três números existentes.

Saída
Para cada linha de entrada, seu programa deve apresentar um valor numérico inteiro, que é a soma dos 3 números existentes 
na linha.

Exemplo de Entrada	Exemplo de Saída
3
Ab23s249ttu21          293
At01v021kkk12           34 
xx14l134mjm01          149





"""