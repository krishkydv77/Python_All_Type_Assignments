#include<stdio.h>
int main(){
    int n=4;
    for(int i=n;i>=1;i--){
        for(int j=n;j>=1;j--){
            if(j<=i) printf("%d ",j);
            else printf("  ");
        }
        printf("\n");
    }
    
    
    
    
    
    return 0;
}