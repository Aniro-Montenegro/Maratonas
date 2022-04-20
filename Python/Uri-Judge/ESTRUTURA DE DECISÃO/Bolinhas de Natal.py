"""
SUBMISSÃO # 26688389
PROBLEMA:3170 - Bolinhas de Natal
RESPOSTA:Accepted
LINGUAGEM:Python 3.8 (Python 3.8.2) [+1s]
TEMPO:0.066s
TAMANHO:211 Bytes
MEMÓRIA:-
SUBMISSÃO:12/03/2022 22:25:09
334	26688389	Aniro Montenegro	Python 3.8	0.066	13/03/2022 01:25:09
"""

bolinhas = int(input())
galhos = int(input())

necessidade = galhos // 2
falta = necessidade - bolinhas
if falta > 0:
    print(f'Faltam {falta} bolinha(s)')
else:
    print('Amelia tem todas bolinhas!')
