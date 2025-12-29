/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{ int n;
    printf("Enter N :");
    scanf("%d",&n);
   for(int i=1;i<=n;i++){
       int temp = 2;
       for(int j=1;j<=n;j++){
           printf("%d ",temp);
           temp +=2;
       }
       printf("\n");
   }

    return 0;
}
