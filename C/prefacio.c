#include <stdio.h>
// a = b × q + r
// 0 ≤ r < |b|
int main()
{
    int a;
    int b;
    int q;
    int r;
    int moduloB;

    scanf("%d %d", &a, &b);
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

    return 0;
}