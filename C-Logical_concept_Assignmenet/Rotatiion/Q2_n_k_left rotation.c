#include <stdio.h>

int main()
{
    int n,k;
    printf("Enter N :");
    scanf("%d",&n);
    printf("Rotation number K :");
    scanf("%d",&k);
    
    int count=0;
    int h=n;
    while(h !=0){
        count++;
        h /=10;
    }
    
    k=k%count;    //bigO ke liye optimaiz kiya
    
    if(k<0) k = k + count;      //nagetive number k dalne pr
    
    
    //power =10^count-1
    int power=1;
    while(count-1 >0){
        power *=10;
        count--;
    }
    int chakkar=0;
    while(k>0){
        chakkar++;
        n=(n%10)*power+ n/10;
        k--;
    }
    printf("%d \n chakkar=%d",n,chakkar);

    return 0;
}