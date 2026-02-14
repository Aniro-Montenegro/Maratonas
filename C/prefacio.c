#include <stdio.h>
<<<<<<< HEAD
=======
// a = b × q + r
// 0 ≤ r < |b|
>>>>>>> ba1cbc6fa399b81bbd89cd7d5aab07dbc563a361
int main()
{
    int a;
    int b;
    int q;
    int r;
    int moduloB;

    scanf("%d %d", &a, &b);
<<<<<<< HEAD
    printf("%d",a);
    printf("%d",b);
=======
    if (b < 0)
    {
        q = b;
        while (1)
        {
            if (a - (b * q) >= 0)
            {
                printf("%d %d\n", q, a - (b * q));
                break;
            }
            else
            {
                q++;
            }
        }
    }
    else
    {
        q = b;
        while (1)
        {
            if (a - (b * q) >= 0)
            {
                printf("%d %d\n", q, a - (b * q));
                break;
            }
            else
            {
                q--;
            }
        }
    }

>>>>>>> ba1cbc6fa399b81bbd89cd7d5aab07dbc563a361
    return 0;
}