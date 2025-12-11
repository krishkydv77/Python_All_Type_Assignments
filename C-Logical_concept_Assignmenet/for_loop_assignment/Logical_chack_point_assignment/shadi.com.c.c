#include <stdio.h>

int main()
{
	char ch;
	int age;
	printf("Enter your gender="); //m for male,f for female
	scanf("%c",&ch);
	printf("Enter your age=");
	scanf("%d",&age);
	if(ch =='m') {
		if(age > 21)
			printf("He can marry");

		else printf("padhai likhai karo ias/yas banno");
	}
	else if(ch =='f') {
		if(age > 18)
			printf("she can marry");

		else printf("chotii bachi ho kya");
	}
	else printf("invalid gender");

	return 0;
}
