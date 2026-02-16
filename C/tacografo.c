#include <stdio.h>

int main()
{
    int n, total, a, b, i;
    scanf("%d", &n);
    total = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%d %d", &a, &b);
        total = total + (a * b);
    }

    printf("%d\n", total);

    return 0;
}