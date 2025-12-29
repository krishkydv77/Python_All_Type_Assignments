#include <stdio.h>

int main()
{ int n;
    printf("Enter N:");
    scanf("%d",&n);
    int temp=(n+ n*n)/2;
    for(int i=n;i>=1;i--){
        
        for(int j=n;j>=i;j--){
            printf("%-2d ",temp--);
        }
        printf("\n");
    }

    return 0;
}