#include <stdio.h>

int main()
{ int n;
    printf("Enter N:");
    scanf("%d",&n);
    int temp=2*(n+n*n)/2 -1;
    for(int i=n;i>=1;--i){
        
        for(int place =1;place <=n-i;++place){
            printf("  ");
        }
        
        for(int j=1;j<=i;++j){
        printf("%d ",temp);
        temp-=2;
        
        }
        printf("\n");
    }

    return 0;
}