#include<stdio.h>
int main() {
	int m,n;
	printf("Enter M:");
	scanf("%d",&m);
	printf("Enter n:");
	scanf("%d",&n);
	for(int num=m; num <=n; num++) {
		int count=0;
		for(int i=2; i*i <=num; i++) {
			if(num%i==0) {
				count++;
				break;
			}
		}
		if(count==0 && num >1) {
			printf("%d ",num);
		}
	}






	return 0;
}