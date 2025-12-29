// 1      
// 12    
// 123  
// 1234

#include <stdio.h>

int main()
{
    int n=4;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j<=i) printf("%d",j);
            else printf("  ");
        }
        printf("\n");
    }

    return 0;
}
