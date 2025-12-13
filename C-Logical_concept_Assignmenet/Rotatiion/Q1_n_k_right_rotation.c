#include <stdio.h>

int main()
{
    int n,k;
    printf("Enter Nuumber :");
    scanf("%d",&n);
    printf("Enter Rotation Number k :");
    scanf("%d",&k);
    
    while(k>0){
        n= (n%10)*10000+ (n/10);
        k--;
    }
    while(k <0){
        n=(n%10000)*10 +(n/10000);
        k++;
    }
printf("%d",n);
    return 0;
}