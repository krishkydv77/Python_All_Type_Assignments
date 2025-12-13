#include <stdio.h>

int main()
{
    int m,n;
    printf("Enter M :");
    scanf("%d",&m);
    printf("Enter N :");
    scanf("%d",&n);
    int i=2;
    int lcm=1;
    int hcf=1;
    while(m>1 || n>1){
        if(m%i==0 ||n%i==0){
            if(m%i==0 && n%i==0) hcf =hcf*i; 
            if(m%i==0) m /=i;
            if(n%i==0) n /=i;
            lcm *=i;
            
        }
        else i++;
    }
    printf("%d",hcf);
   printf("\nlcm : %d",lcm);

 



    return 0;
}
