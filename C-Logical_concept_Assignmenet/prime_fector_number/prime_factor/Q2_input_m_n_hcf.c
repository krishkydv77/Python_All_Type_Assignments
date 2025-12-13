#include <stdio.h>

int main(){
int m,n,hcf;
printf("Enter M :");
scanf("%d",&m);
printf("Enter n :");
scanf("%d",&n);
hcf=m;
while(1){
    if(m % hcf == 0 && n % hcf == 0){
        printf("%d, %d hcf : %d",m,n,hcf);
        break;
    }
    hcf--;
}
    return 0;
}
