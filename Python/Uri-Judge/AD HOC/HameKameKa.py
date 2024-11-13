""""
SUBMISSÃO # 26688767
PROBLEMA:2591 - HameKameKa
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.112s
TAMANHO:446 Bytes
MEMÓRIA:-
SUBMISSÃO:12/03/2022 23:00:3
306	26688767	Aniro Montenegro	Python 3.8	0.112	13/03/2022 02:00:34

"""

n = int(input())

for _ in range(n):
    palavra = input()
    numero1 = 0
    numero2 = 0
    ref = 0
    for l in palavra:
        if l != 'a' and ref == 0:
            ref = 1

        elif l != 'a' and ref == 1:
            ref = 2

        if l == 'a' and (ref == 1 or ref == 0):
            numero1 += 1
        elif l == 'a' and ref == 2:
            numero2 += 1
    aq = 'a' * (numero2 * numero1)
    print(f'k{aq}')
