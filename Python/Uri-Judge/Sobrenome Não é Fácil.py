n = int(input())
for _ in range(n):
    palavra = input()
    lista = ['a', 'e', 'i', 'o', 'u']
    total = 0
    tamanho = len(palavra)
    i = 0
    while i < tamanho:
        if palavra[i].lower() not in lista:
            total = 1
            x = i + 1
            while x < tamanho:
                if palavra[x].lower() not in lista:
                    total = total + 1
                    x += 1
                    if total >= 3:
                        i = tamanho + 1
                        break
                else:
                    total = 0
                    break
        i += 1

    if total >= 3:
        print(palavra+' nao eh facil')
    else:
        print(palavra+' eh facil')


"""
RANKING
5	26127430	Aniro Montenegro	Python 3	0.000	03/02/2022 05:40:13


SUBMISSÃO # 26127430
PROBLEMA:
3358 - Sobrenome Não é Fácil
RESPOSTA:
Accepted
LINGUAGEM:
Python 3.8 (Python 3.8.2) [+1s]
TEMPO:
0.000s
TAMANHO:
735 Bytes
MEMÓRIA:
-
SUBMISSÃO:
03/02/2022 02:47:14

"""


"""
A região sul do Brasil é caracterizada pela ascendência multicultural de seus habitantes, sendo principalmente europeus
 e sobretudo italianos, alemães e poloneses. Uma consequência interessante disso é a variação na dificuldade na 
 pronúncia dos sobrenomes da população, o que as vezes dificulta a vida dos professores na realização da chamada de 
 sua turma, gerando até situações constrangedoras. Dada a possibilidade de constrangimento em suas aulas, a professora 
 Jiraiya decidiu pesquisar os sobrenomes em sua lista de chamadas. Na concepção de Jiraiya, um sobrenome é difícil se 
 tiver três ou mais consoantes consecutivas.

Entrada
A entrada contém vários casos de teste. A primeira linha possui um inteiro N que indica o número de casos de teste. 
Cada caso de teste consiste em um sobrenome. A string contém letras do alfabeto sem acentos, a primeira letra está 
sempre em maiúscula e o sobrenome pode ter no máximo 42 caracteres.

Saída
Para cada caso de entrada, imprima o sobrenome e se é fácil ou não, conforme mostra o exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
6
Ferrari             Ferrari eh facil
Bianchi             Bianchi nao eh facil
Hoffmann            Hoffmann nao eh facil
Hofmann             Hofmann eh facil
Lewandowski         Lewandowski nao eh facil
Nowak               Lewandowski nao eh facil

"""