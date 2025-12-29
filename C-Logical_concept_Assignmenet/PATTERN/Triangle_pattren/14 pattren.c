#include <stdio.h>

int main()
{ int n;
    printf("Enter N:");
    scanf("%d",&n);
    int temp=(n+n*n)/2;
    for(int i=1;i<=n;i++){
    for(int j=n;j>=i;j--){
        printf("%-2d ",temp);
        temp--;
            
        }
        printf("\n");
    }

    return 0;
}