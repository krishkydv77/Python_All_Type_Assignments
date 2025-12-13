#include <stdio.h>

int main()
{
    int n;
    printf("Enter N:");
    scanf("%d",&n);
    int i=2;
    while(i <=n){
        while(n%i==0){
            printf("%d ",i);
            n /=i;
        }
        i++;
    }

    return 0;
}