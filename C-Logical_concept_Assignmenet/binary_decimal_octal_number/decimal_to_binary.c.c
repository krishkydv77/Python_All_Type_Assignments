#include <stdio.h>

//"Write a C program to convert a decimal number into its binary equivalent without using arrays or strings."

int main()
{
	int n,mod,binary=0,stap=1;
	printf("Enter number :");
	scanf("%d",&n);
	while(n>0) {
		mod=n%2;
		binary = binary + mod*stap;
		n /=2;
		stap *=10;
	}
	printf("%d",binary);




	return 0;
}