//1. Write a c program to calculate the sum of the first N natural number using a while loop.
#include <stdio.h>

int main()
{	int n,sum=0;
	printf("Enter number: ");
	scanf("%d",&n);
	int i=1;
	while(i<=n) {
		sum +=i;
		i++;
	}
	printf("sum= %d",sum);

	return 0;
}

//2. Write a C program to input the age of a person and check if they are eligible to vote(age>=18).

#include <stdio.h>
int main(){
    int age;
    printf("Enter your age :");
    scanf("%d",&age);
    if(age>=18) printf("valid vote");
    else printf("not valid vote");
    
    return 0;
}

//3.  write a c program to print the multipalication for a user-input number.

#include <stdio.h>
int main()
{ int n,table;
    printf("Enter n:");
    scanf("%d",&n);
    for(int i=1;i<=10;i++){
        table=n*i;
        printf("%2d * %2d = %2d",n,i,table);
        printf("\n");
    } 

    return 0;
}

//4. write a C program to assign grades based on marks using the following criteria: 90-100=A,80-89=B,70-79=C,60-69=D,below 60=fail.

#include <stdio.h>
int main(){
int mark;
printf("Enter Marks: ");
scanf("%d",&mark);
if(mark>=90) printf("A");
else if(mark>=80 && mark<=89) printf("B");
else if(mark>=70 && mark <=79) printf("C");
else if(mark>=60 && mark <=69) printf("D");
else printf("Fail");

return 0;
}

//5. write a c program to calculate the factorial of a given number.

#include <stdio.h>
int main()
{ int n;
    printf("Enter n:");
    scanf("%d",&n);
    int fectorial=1;
    for(int i=1;i<=n;i++){
        fectorial *=i;
    }
    printf("%d",fectorial);

    return 0;
}

//6. Write a C program to check if a number is a palindrome using a while loop.

#include<stdio.h>
int main(){
    int number,revers=0,rem;
    printf("Enter Number : ");
    scanf("%d",&number);
    int temp=number;
    while(number !=0){
        revers = revers*10 +(number%10);
        number/=10;
    }
    if(temp==revers) printf("palindrome");
    else printf("Not palindrome");
    return 0;
}

//7. write a c program to find the sum of digits of a given number.

#include <stdio.h>

int main()
{ int n,sum=0;
    printf("Enter number :");
    scanf("%d",&n);
    for(int i;n>=1; ){
        i=n%10;
        sum +=i;
        n /=10;
        
    }
    printf("sum: %d",sum);

    return 0;
}

//8.Write a program to print the first N Fibonacci numbers using a while loop.

#include<stdio.h>
int main(){
	int a=0,b=1,n;
	printf("Enter n:");
	scanf("%d",&n);
	while(n >=1) {
		printf("%d %d ",a,b);
		a=a+b;
		b=a+b;

		n--;
	}

	//method 2
	int n,fibonacci;
	printf("Enter Number :");
	scanf("%d",&n);
	int i=1;
	int a=0;
	int b=1;
	printf(" %d %d ",a,b);
	int nxt;
	while(i <=n) {
		nxt = a+b;
		printf("%d ",nxt);
		a=b;
		b=nxt;
		i++;

	}
	
	return 0;
}

//9. Write a c program to print all prime number b/w 1 and n.

#include <stdio.h>
int main()
{ int n,prime=0,count=0;
    printf("Enter N:");
    scanf("%d",&n);
  for(int i=2;i<n;i++){
      int count=0;
      for(int p=2;p<i;p++){
          if(i%p==0){
              count++;}
      }
      if(count==0){
          printf("%d ",i);
          prime++;
      }
       
  }
  printf("prime: %d",prime);

    return 0;
}

//10. Write a C program to print following pattern when n=4.
 /*1 2 3 4
   5 6 7 8
   9101112
   13141516 */

#include <stdio.h>
int main()
{ int n;
    printf("Enter n:");
    scanf("%d",&n);
    int temp=1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            printf("%2d",temp);
            temp++;
        }
        printf("\n");
    }

    return 0;
}


//11. write a function in c to find greatest number of three number.

#include <stdio.h>
int main()
{	int a,b,c;
	printf("Enter 3 number :");
	scanf("%d %d %d",&a,&b,&c);
	if(a>=b && a>=c) {
		printf("greater %d",a);
	}
	else if(b>=a && b>=c) {
		printf("greater %d",b);
	}

	else printf("greater %d",c);

	return 0;
}


//12. Write a C program to print following pattern when n=6(hollow trianguler)
          1           
        2   2         
      3       3       
    4           4     
  5               5   
6 5 4 3 2 1 2 3 4 5 6 

#include <stdio.h>
int main()
{ int n=6;
    // printf("Enter N:");
    // scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=n;j>=1;j--){
            if(i==n || j==i) printf("%d ",j);
            else printf("  ");
        }
        for(int j=2;j<=n;j++){
            if(i==n || i==j) printf("%d ",j);
            else printf("  ");
        }
        printf("\n");
    }

    return 0;
}


//13. Electrical bill amount

#include <stdio.h>
int main() {
	int units, i;
	float billamount = 0.0;
	float rate;

	printf("Enter total units consumed: ");
	scanf("%d", &units);

	for (i = 1; i <= units; i++) {
		if (i <= 100) {
			rate = 1.50;
		} else if (i <= 200) {
			rate = 2.00;
		} else if (i <= 300) {
			rate = 3.00;
		} else {
			rate = 5.00;
		}
		billamount += rate;
	}

	printf("Electricity Bill = Rs. %.2f", billamount);

	return 0;
}










