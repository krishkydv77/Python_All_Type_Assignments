#include <stdio.h>

int main()
{ int n;
    printf("Enter N:");
    scanf("%d",&n);
    
    for(int i=n;i>=1;i--){
        
        for(int j=1;j<=i;j++){
            printf("%-2d ",i);
            
            
        }
        printf("\n");
    }

    return 0;
}