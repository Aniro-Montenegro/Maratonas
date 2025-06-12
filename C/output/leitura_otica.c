#include <stdio.h>
#include <stdlib.h>

int main()
{

    int n;
    int vetor[5];
    int indice;
    int i;
    int x;
    int menor;
    int quantidade;
    int maior;
    int media;

    while (1)
    {
        scanf("%d", &n);
        if (n == 0)
        {
            break;
        }
        else
        {
            for (x = 0; x < n; x++)
            {
                menor = 256;
                quantidade = 0;
                for (i = 0; i < 5; i++)
                {
                    scanf("%d", &vetor[i]);
                    if (vetor[i] <= 127)
                    {
                        menor = vetor[i];
                        indice = i;
                        quantidade++;
                    }
                }

                if (quantidade != 1)
                {
                    printf("*\n");
                }
                else if (indice == 0)
                {
                    printf("A\n");
                }
                else if (indice == 1)
                {
                    printf("B\n");
                }
                else if (indice == 2)
                {
                    printf("C\n");
                }
                else if (indice == 3)
                {
                    printf("D\n");
                }
                else if (indice == 4)
                {
                    printf("E\n");
                }
            }
        }
    }

    return 0;
}