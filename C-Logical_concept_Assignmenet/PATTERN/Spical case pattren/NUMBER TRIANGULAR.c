#include<stdio.h>
int main(){
    int n=4;
    for(int i=1;i<=n;i++){
        for(int j=n;j>=1;j--){
            if(j<=i) printf("%d   ",i);
            else printf ("  ");
        }
        printf("\n");
    }
}