#include <stdio.h>

int main()
{
    int n;
    printf("Enter N:");
    scanf("%d",&n);
   
   int prime=0;
   for(int i=2;i<n;i++){
       int count=0;
       for(int p=2;p<i;p++){
           if(i%p==0){
               count++;
           }
           
       }
       if(count==0) {
           printf("%d ",i);
           prime++;}
       
       
   }
   printf("prime : %d",prime);
   
    return 0;
}
