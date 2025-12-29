#include<stdio.h>
int main(){
    int n;
    printf("Enter N:");
    scanf("%d",&n);
    // for(int i=1;i<=n;i++){
    //     for(int j=1;j<=i;j++){
    //         printf("*");
    //     }
    //     printf("\n");
    // }
    //  for(int i=1;i<=n;i++){
    //     for(int j=n;j>=i;j--){
    //         printf("*");
    //     }
    //     printf("\n");
    // }
    
    // for(int i=1;i<=n;i++){
    //     for(int place=1;place<=n-i;place++){
    //         printf("  ");
    //     }
    //     for(int j=1;j<=i;j++){
    //         printf("* ");
    //     }
    //     printf("\n");
    // }
    
    for(int i=n;i>=1;--i){
        for(int place=1;place<=n-i;++place){
            printf("  ");
        }
        for(int j=1;j<=i;++j){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}