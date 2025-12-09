
#include <stdio.h>

int main()
{
	//Q) write a c program input number and check number is greater than 10 or not ?
	int a;
	printf("Enter number=");
	scanf("%d",&a);
	if(a>10) {
		printf("vaild number");
	}
	else printf("invalid number");

	//Q) write a c program input number and check number is greater than 67 or not ?
	int a;
	printf("Enter number=");
	scanf("%d",&a);
	if(a>67) printf("vaild number");
	else printf("invalid number");

	//Q) write a c program input number and check number is even or odd ?
	int a;
	printf("Enter number=");
	scanf("%d",&a);
	if(a%2==0) printf("even number");
	else printf("odd number");

	//Q) write a c program input number and check number is divisible by 5 or not ?
	int a;
	printf("Enter number=");
	scanf("%d",&a);
	if(a%5==0) printf("divisible by 5");
	else printf("not divisible by 5");

	//Q) write a c program input character :a (apple),otherwise :input is not matched
	char ch;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='a') printf("apple");
	else printf("input is not matched");

	//Q) write a c program input character :b (ball),otherwise :input is not matched
	char ch;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='b') printf("ball");
	else printf("input is not matched");

	//Q) write a c program input character and check character is vowel and consonant ?
	char ch;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch =='a') printf("vowel");
	else if (ch =='e') printf("vowel");
	else if (ch =='i') printf("vowel");
	else if (ch =='o') printf("vowel");
	else if (ch =='u') printf("vowel");
	else printf("consonant");

	//Q) write a c program input character and check character is q,w,e,r,t,y,u,i,o,p : upper line ,otherwise :input is not matched
	char ch;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch == 'q') {
		printf("upper line");

	}
	else {
		if (ch == 'w') {
			printf("upper line");
		}
		else {
			if(ch == 'e') {
				printf("upper line");
			}
			else {
				if(ch =='r') {
					printf("upper line");
				}
				else {
					if(ch == 't') {
						printf("upper line");
					}
					else {
						if(ch=='y') {
							printf("upper line");
						}
						else {
							if(ch =='u') {
								printf("upper line");
							}
							else {
								if(ch == 'i') {
									printf("upper line");
								}
								else {
									if(ch == 'o') {
										printf("upper line");
									}
									else {
										if(ch =='p') {
											printf("upper line");
										}
										else {
											printf("input is not match");

										}
									}
								}
							}
						}
					}
				}
			}
		}
	}

	//Q) write a c program input character and check character is a,s,d,f,g,h,j,k,l : mid line, otherwise :input is not matched
	char ch;
	printf("Enter character=");
	scanf("%c",&ch);
	int regex=0;
	if(ch == 'a') {
		regex=1;
	}
	if(ch == 's') {
		regex=1;
	}
	if(ch == 'd') {
		regex=1;
	}
	if(ch == 'f') {
		regex=1;
	}
	if(ch == 'g') {
		regex=1;
	}
	if(ch == 'h') {
		regex=1;
	}
	if(ch == 'j') {
		regex=1;
	}
	if(ch == 'k') {
		regex=1;
	}
	if(ch == 'l') {
		regex=1;
	}
	if(regex == 1) {
		printf("mid line");
	}
	else {
		printf("input is not match");
	}

	//Q) write a c program input character and check character is z,x,c,v,b,n,m : lower line, otherwise :input is not matched
	char ch;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch == 'z') {
		printf("lower line \n");
		return 0;

	}
	if(ch == 'x') {
		printf("lower line \n");
		return 0;

	}
	if(ch == 'c') {
		printf("lower line \n");
		return 0;
	}
	if(ch == 'v') {
		printf("lower line \n");
		return 0;
	}
	if(ch == 'b') {
		printf("lower line \n");
		return 0;
	}
	if(ch == 'n') {
		printf("lower line \n");
		return 0;
	}
	if(ch == 'm') {
		printf("lower line \n");
		return 0;
	}
	else {
		printf("input is not matched");
	}

	//Q) write a c program input character 'a':two number(addition),otherwise :input is not matched
	char ch;
	int n1,n2,nt;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='a') {
		printf("Enter number n1 =");
		scanf("%d",&n1);
		printf("Enter number n2=");
		scanf("%d",&n2);
		nt=n1+n2;
		printf("addition: %d",nt);
	}
	else printf("input is not matched");

	//Q) write a c program input character 's': two number (substraction),otherwise :input is not matched
	char ch;
	int n1,n2,nt;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='s') {
		printf("Enter number n1 =");
		scanf("%d",&n1);
		printf("Enter number n2=");
		scanf("%d",&n2);
		nt=n1-n2;
		printf("substraction: %d",nt);
	}
	else printf("input is not matched");

	//Q) write a c program input character 'm':two number(multiplication),otherwise :input is not matched
	char ch;
	int n1,n2,nt;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='m') {
		printf("Enter number n1 =");
		scanf("%d",&n1);
		printf("Enter number n2=");
		scanf("%d",&n2);
		nt=n1*n2;
		printf("multiplication: %d",nt);
	}
	else printf("input is not matched");

	//Q) write a c program input character 'd':two number(divide),otherwise :input is not matched
	char ch;
	int n1,n2,nt;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='d') {
		printf("Enter number n1 =");
		scanf("%d",&n1);
		printf("Enter number n2=");
		scanf("%d",&n2);
		nt=n1/n2;
		printf("divide: %d",nt);
	}
	else printf("input is not matched");

	//Q) write a c program input character 's':two number >>swap number without third variable,otherwise :input is not matched
	char ch;
	int n1,n2;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='s') {
		printf("Enter n1=");
		scanf("%d",&n1);
		printf("Enter n2=");
		scanf("%d",&n2);
		n1=n1+n2;
		n2=n1-n2;
		n1=n1-n2;
		printf("n1= %d and n2= %d ",n1,n2);
	}
	else printf("input is not matched");

	//Q) write a c program input character 'w':two number >>swap number with third variable,otherwise :input is not matched
	char ch;
	int n1,n2,n3;
	printf("Enter character=");
	scanf("%c",&ch);
	if(ch=='w') {
		printf("Enter n1=");
		scanf("%d",&n1);
		printf("Enter n2=");
		scanf("%d",&n2);
		n3=n1;
		n1=n2;
		n2=n3;

		printf("n1= %d and n2= %d ",n1,n2);
	}
	else printf("input is not matched");

	//Extra Question for logical

	// q.1 :- Write Play station code using "AND" & "OR" operation . Where condition is marks >= 90 and position == 1 (marks and position are user input)
	int m,p;   //m =marks, p= position
	printf("Enter marks=");
	scanf("%d",&m);
	printf("Enter your class position=");
	scanf("%d",&p);

	//use and operator
	if(m >=90 && p ==1) {
		printf("Play station");
	}
	else printf("next time milega");

	// use or operator      (if you want or operator, and operator code comment use)
	/* if(m >= 90 || p ==1){
	     printf("Play station");
	 }
	 else printf("netx time milega"); */

	return 0;
}