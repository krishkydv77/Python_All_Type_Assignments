#include <stdio.h>

int main()
{ int n;
    printf("Enter N:");
    scanf("%d",&n);
    
    for(int i=1;i<=n;i++){
        int temp=1;
        for(int j=n;j>=i;j--){
            printf("%-2d ",temp);
            temp++;
            
        }
        printf("\n");
    }

    return 0;
}