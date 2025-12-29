#include<stdio.h>
int main(){
    int n;
    printf("Enter N:");
    scanf("%d",&n);
    char ch='P';
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%c ",ch);
            ch--;
        }
        printf("\n");
    }
    
    
    
    return 0;
}
