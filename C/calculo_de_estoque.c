
/*Descrição
Uma empresa de varejo que vende produtos pela internet deseja saber o valor total em estoque que ela mantêm em mercadorias nos N centros de distribuição existentes. Para isso, precisa desenvolver uma solução computacional para fazer esse cálculo. E você será a pessoa responsável por isso.

Entrada
Inicialmente um valor N é informado, indicando a quantidade de centros de distribuição a serem processados. Cada centro de distribuição inicia com um inteiro P indicando a quantidade de tipos de produtos em estoque. Seguem P linhas cada uma um inteiro Q e um inteiro V, separados por um espaço em branco, representando a quantidade de um tipo de produto e o valor unitário do produto, respectivamente.

 

Saída
Para cada centro de distribuição, imprima o valor total em estoque, e por fim o valor total em todos os centros de distribuição.*/


#include <stdio.h>

int main()
{
   int n,t,a,b,total,i,x,g=0;
   
   scanf("%d",&n);

for(i=0;i<n;i++){
    
    scanf("%d",&t);
    total=0;
    
    for(x=0;x<t;x++){
        scanf("%d %d",&a,&b);
        total+=(a*b);
    }
            g+=total;

    
    printf("%d\n",total);


    
}
    printf("%d\n",g);

   

    return 0;
}
