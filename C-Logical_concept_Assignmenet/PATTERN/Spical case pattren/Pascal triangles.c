#include <stdio.h>

int main()
{
    int n=4; 
    for(int i=0;i<=n;i++){
        int pac=1;
        for(int j=0;j<=n;j++){
            if(j< n-i) printf(" ");
            else{ printf("%d ",pac);
            pac = pac * (i - (j - (n - i))) / ((j - (n - i)) + 1);}    //col=j-(n-i)
            
        }
        printf("\n");
    }

    return 0;
}



// pascal formula  pac(1)=pac*(i-col)/(col+1)