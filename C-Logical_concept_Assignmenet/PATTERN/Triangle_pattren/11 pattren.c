#include <stdio.h>

int main()
{ int n;
    printf("Enter N:");
    scanf("%d",&n);
    
    for(int i=1;i<=n;i++){
        
        for(int j=n;j>=i;j--){
            printf("%-2d ",i);
            
            
        }
        printf("\n");
    }

    return 0;
}