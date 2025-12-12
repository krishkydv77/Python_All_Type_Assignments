#include <stdio.h>

int main()
{
    int n,m;
    printf("Enter M : ");
    scanf("%d",&m);
    printf("Enter N : ");
    scanf("%d",&n);
    int i=2;
    while(m>1 || n>1){
        if(m%i==0 || n%i==0){
            if(m%i==0) m /=i;
            if(n%i==0) n /=i;
            printf("%d ",i);
        }
        else i++;
    }

    return 0;
}