#include <stdio.h>

int main()
{
	// q.1 :- Write Play station code using "AND" & "OR" operation . Where condition is marks >= 90 and position == 1 (marks and position are user input)
	int m,p;   //m =marks, p= position
	printf("Enter marks=");
	scanf("%d",&m);
	printf("Enter your class position=");
	scanf("%d",&p);

	// AND operator
	/* if(m >=90 && p ==1){
	     printf("Play station");
	 }
	 else printf("next time milega"); */


	//OR operator

	if(m >= 90 || p ==1) {
		printf("Play station");
	}
	else printf("netx time milega");


	return 0;
}