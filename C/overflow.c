#include <stdio.h>

int main()
{
     long long n, total, a, b;
    char simbolo;
    scanf("%lld", &n);
    scanf("%lld %c %lld", &a,&simbolo,&b);
    total = 0;
    if(simbolo=='*'){
        total=a*b;
    }
    if(simbolo=='+'){
        total=a+b;
    }

    if(total<=n){
        printf("OK\n");
    }
    else{
        printf("OVERFLOW\n");
    }

 

    return 0;
}