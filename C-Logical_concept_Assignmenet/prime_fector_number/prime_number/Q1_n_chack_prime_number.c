#include <stdio.h>

int main()
{  int n;
    printf("Enter N :");
    scanf("%d",&n);
    int count=0,loop=0;
    for(int i=2;i*i<n;i++){            // sqrot(n) se choti number se hi baag ja skta ha n me
        loop++;
        if(n%i==0){
            printf("%d ",i);
            count++;
        }
    }
    printf("loop: %d \n",loop);
    if(count==0) printf("prime number");
    else printf("not prime number");

    return 0;
}