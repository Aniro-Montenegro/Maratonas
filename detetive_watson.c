/*
Descrição
John Watson, mesmo após anos trabalhando ao lado de Sherlock Holmes, nunca conseguiu entender como ele consegue descobrir quem é o assassino com tanta facilidade. Em uma certa noite, porém, Sherlock bebeu mais do que devia e acabou contando o segredo a John.

“É estupidamente fácil”, disse Sherlock Holmes. “Nunca é o mais suspeito, mas sim o segundo mais suspeito”. Após descobrir o segredo, John decidiu resolver um crime por conta própria, só para testar se aquilo fazia sentido ou se era apenas conversa de bêbado.

Dada uma lista com N inteiros, representando o quanto cada pessoa é suspeita, ajude John Watson a decidir quem é o assassino, de acordo com o método citado.

Entrada
Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro N (2 ≤ N ≤ 1000), representando o número de suspeitos.

Em seguida haverá N inteiros distintos, onde o i-ésimo inteiro, para todo 1 ≤ i ≤ N, representa o quão suspeita a i-ésima pessoa é, de acordo com a classificação dada por John Watson. Seja V o valor do i-ésimo inteiro, 1 ≤ V ≤ 10000.

O último caso de teste é indicado quando N = 0, o qual não deverá ser processado.

Saída
Para cada caso de teste imprima uma linha, contendo um inteiro, representando o indice do assassino, de acordo com o método citado.


Exemplos de Entrada	Exemplos de Saída
3
3 5 2
5
1 15 3 5 2
0

1
4
*/


#include <stdio.h>
#include <stdlib.h>

void ordena(int v[],int n)
{
     int gap=n-1,i=0,aux;
    while(i<n)
    {
        for(i=0;i+gap<n;i++)
        {
            if(v[i]<v[i+gap])
            {
                aux=v[i];
                v[i]=v[i+gap];
                v[i+gap]=aux;

            }

        }
        gap--;
    }

}

int main()
{
   int *v,*p,i,n=1,z,ind=0,x;
   scanf("%d",&n);
   while (n!=0)
   {

       v=malloc(sizeof(int)*n);
       p=malloc(sizeof(int)*n);
       for(i=0;i<n;i++)
       {
           scanf("%d",&v[i]);
           p[i]=v[i];
       }
       ordena(v,n);
        x=v[1];
        for(i=0;i<n;i++)
        if(p[i]==v[1])
       {
           printf("%d\n",i+1);
           ind=1;
           break;
       }


    ind=0;
    scanf("%d",&n);
   }
    return 0;
}
