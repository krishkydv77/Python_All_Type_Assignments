#include <stdio.h>

int main()
{
    int n=5;
   for(int i=1;i<=n;i++){
       for(int j=n;j>=1;j--){
           if(j==i || i==n) printf("* ");
           else printf("  ");
       }
           
           for(int j=2;j<=n;j++){
               if(j==i || i==n) printf("* ");
               else printf("  ");
           }
       
       printf("\n");
   }
    return 0;
}