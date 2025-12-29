#include <stdio.h>

int main()
{ int n;
    printf("Enter N :");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int place=1;place <=n-i;place++){
        
            printf("  ");
        }
            for(int j=i;j>=1;j--){
                printf("%d ",i);
            }
        
        printf("\n");
    }

    return 0;
}