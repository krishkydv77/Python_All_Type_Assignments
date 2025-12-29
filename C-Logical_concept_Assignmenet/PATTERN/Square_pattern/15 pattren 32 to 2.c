#include <stdio.h>

int main()
{int n;
    printf("Enter N :");
    scanf("%d",&n);
   int temp=2*n*n;
    for(int i=1;i<=n;i++){
        
        for(int j=n;j>=1;j--){
            printf("%d ",temp);
          temp-=2;
        }
        printf("\n");
    }
    return 0;
}