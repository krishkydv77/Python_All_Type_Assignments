
#include <stdio.h>

int main()
{
//1. print 1-100
	int i=1;
	while(i <=100) {
		printf("%d ",i);
		i++;
	}
//2. print 100-1
	int i=100;
	while(i>=1) {
		printf("%d ",i);
		i--;
	}

//3. print 1-n
	int i=1,n=100;
	while(i <=n) {
		printf("%d ",i);
		i++;
	}

//4. print n-1
	int n=200;
	while(n >=1) {
		printf("%d ",n);
		n--;
	}

//5.m-n (m,n user input)
	int m,n;
	printf("Enter m:");
	scanf("%d",&m);
	printf("Enter n:");
	scanf("%d",&n);
	while(m<=n) {
		printf("%d ",m);
		m++;
	}

//6. n-m print
	int m,n;
	printf("Enter m:");
	scanf("%d",&m);
	printf("Enter n:");
	scanf("%d",&n);
	while(m >=n) {
		printf("%d ",m);
		m--;
	}

//7. 1-100 even and old number
	int i=1;
	while(i <=100) {
		if(i%2==0) {
			printf("%d ",i);
		}
		i++;
	}


//odd number
	/*int i=1;
	while(i <=100){
	    if(i%2 != 0){
	        printf("%d ",i);
	    }
	    i++;
	} */

//8.100 -1 even number
	int i=100;
	while(i>=1) {
		if(i%2==0) {
			printf("%d ",i);
		}
		i--;
	}

//9. m-n even/odd
	int m,n;
	printf("Enter m:");
	scanf("%d",&m);
	printf("Enter n:");
	scanf("%d",&n);
	while(m <= n) {
		if(m%2==0) {
			printf("%d ",m);
		}
		m++;
	}


//odd number
	/*int m,n;
	printf("Enter m:");
	scanf("%d",&m);
	printf("Enter n:");
	scanf("%d",&n);
	while(m <= n){
	    if(m%2 !=0){
	        printf("%d ",m);
	    }
	    m++;
	} */

//10. 1-500
	int n,i=1;
	printf("Enter N: ");
	scanf("%d",&n);
	while(i <=500) {
		if(i%n==0) {
			printf("%d ",i);
		}
		i++;
	}


	return 0;
}
