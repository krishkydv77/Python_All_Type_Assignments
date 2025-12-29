#include <stdio.h>

int main()
{
     int n;
    printf("Enter N:");
    scanf("%d",&n);
    int temp=2*(n+n*n)/2;
    for(int i=1;i<=n;i++){
        for(int place=1;place<=(n-i);place++){
            printf("  ");
        }
        for(int j=1;j<=i;j++){
            printf("%2d",temp);
            temp-=2;
        }
        printf("\n");
    }

    return 0;
}