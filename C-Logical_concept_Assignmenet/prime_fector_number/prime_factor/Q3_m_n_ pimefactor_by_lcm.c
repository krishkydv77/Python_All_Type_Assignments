
#include <stdio.h>

int main()
{ int m,n;
    printf("Enter M:");
    scanf("%d",&m);
    printf("Enter n:");
    scanf("%d",&n);
    int prod =1;
    int i=2;
    while(1 <m || 1<n){
        if(m%i==0 || n%i==0){
            if(m%i==0) m /=i;
            if(n%i==0) n /=i;
           printf(" %d ",i);
            prod *=i;
            
            
        }
       
        else i++;
    }
     
     printf("\n lcm :%d ",prod);

    return 0;
}
