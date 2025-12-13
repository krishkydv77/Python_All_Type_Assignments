#include <stdio.h>

int main()
{	int n;
	printf("Enter Number :");
	scanf("%d",&n);
	int i=1;
	while(i*i<=n) {
	//while(i*i*i<=n)     //if you should cube 
		i++;
	}
	i--;
	printf("%d",i);

	return 0;
}
