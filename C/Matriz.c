/*
Descrição
Imagine que exista uma matriz de ordem 3 em Java com os seguintes valores correspondentes aos preços de determinados itens disponíveis para comercialização em um e-commerce recém inaugurado na região do município de Franca:



Elabore um programa responsável por exibir o somatório dos preços dos itens presentes na diagonal principal e diagonal secundária.

Entrada
A entrada é composta por três linhas da matriz, cada linha contém três valores com duas casas decimais. Cada valor obedece a desigualdade 0 < valor < 100.

Saída
A saída deve conter duas linhas. Na primeira linha deve ser impressa a mensagem "DIAGONAL PRINCIPAL" seguida pelos valores com duas casas decimais da diagonal principal, separados por um espaço em branco. Ao final da primeira linha imprima o resultado da soma. Exemplo:

DIAGONAL PRINCIPAL 11.50 22.20 33.55 67.25

Na segunda linha, faça a mesma coisa que na primeira, mas com os valores da diagonal SECUNDÁRIA. Exemplo:
DIAGONAL SECUNDARIA 13.45 22.20 31.50 67.15

Perceba que a palavra "secundária" não deve conter acento na saída.


Exemplos de Entrada	
11.50 12.80 13.45
21.10 22.20 23.30
31.50 32.90 33.55

Exemplos de Saída
DIAGONAL PRINCIPAL 11.50 22.20 33.55 67.25
DIAGONAL SECUNDARIA 13.45 22.20 31.50 67.15
*/

#include <stdio.h>

int main()
{
    float mat[3][3];
    float s1,s2;
    
    int i,j;
    
    for(i=0;i<3;i++){
        
        for(j=0;j<3;j++){
            scanf("%f",&mat[i][j]);
        }
    }
    
    s1=mat[0][0]+mat[1][1]+mat[2][2];
    s2=mat[0][2]+mat[1][1]+mat[2][0];
    
    printf("DIAGONAL PRINCIPAL %.2f %.2f %.2f %.2f\n",mat[0][0],mat[1][1],mat[2][2],s1);
    printf("DIAGONAL SECUNDARIA %.2f %.2f %.2f %.2f\n",mat[0][2],mat[1][1],mat[2][0],s2);

    return 0;
}
