#include <stdio.h>

int main()
{
    //Basic Loop Concepts


	// 1. Write a program to print the numbers from 1 to 10 using a while loop.
	int i=1;
	while(i <=10) {
		printf("%d ",i);
		i++;
	}

	//2. Print the even numbers from 2 to 20 using a while loop.
	int i=1;
	while(i <=20) {
		if(i%2 ==0) {
			printf("%d ",i);
		}
		i++;
	}

	//3. Write a program to print the odd numbers from 1 to 20 using a while loop.
	int i=1;
	while(i <=20) {
		if(i%2 !=0) {
			printf("%d ",i);
		}
		i++;
	}

	//4. Write a program to print all integers between 10 and 1 in reverse order using a while loop.
	int i=10;
	while(i >=1) {
		printf("%d ",i);
		i--;
	}

	//5. Write a program to print the numbers 1 to 100, but only print those that are divisible by 5.
	int i=1;
	while(i <=100) {
		if(i%5 ==0) {
			printf("%d ",i);
		}
		i++;
	}





    //Sum and Average Calculations

    //6. Write a program that computes the sum of integers from 1 to N, where N is provided by the user.
	int i=1,sum=0,n;
	printf("Enter N: ");
	scanf("%d",&n);

	while(i <= n) {
		sum +=i;
		i++;
	}
	printf("%d ",sum);

//7. Write a program to compute the sum of all even numbers between 1 and 100.
	int i=1,sum=0;
	while(i <=100) {
		if(i%2==0) {
			sum +=i;
		}
		i++;
	}
	printf("%d ",sum);

//8. Write a program to compute the sum of digits of a given number.
	int i,sum=0,digit;
	printf("Enter Digit: ");
	scanf("%d",digit);
	while(digit !=0) {
		i = digit%10;
		sum += i;
		digit /= 10;
	}
	printf("%d",sum);

	//9. Write a program to calculate the average of N numbers entered by the user.
	float n,sum=0;
	int i=1;
	printf("Enter N :");
	scanf("%f",&n);
	while(i <= n) {
		sum += i;
		i++;
	}

	printf("avg: %f ",sum/n);

	//10. Write a program that sums all the multiples of 7 between 1 and 500.
	int i=1,sum=0,n=500;
	while(i <=500) {     //while(i <=500)
		if(i%7 ==0) {
			sum +=i;
		}
		i++;
	}
	printf("%d ",sum);



    //Factorials and Mathematical Problems


    //11. Write a program to compute the factorial of a given number using a while loop.
	int i=1,f,r=1;       //multiplai number always 1. 
	printf("Enter number =");
	scanf("%d",&f);
	while(i <= f) {
		r *= i;
		i++;
	}
	printf("%d ",r);

//12. Write a program to find the product of all odd numbers from 1 to N.
	int i=1,pro=1,n;
	printf("Enter N: ");
	scanf("%d",&n);
	while(i <=n) {
		if(i%2 != 0) {
			pro *=i;
		}
		i++;
	}
	printf("%d ",pro);

//13.Write a program to check whether a number is a prime number.
	int n;
	printf("Enter Number :");
	scanf("%d",&n);
	int i=1;
	int count =0;
	while(i <n) {              // if <= use then count==2
		if(n%i==0) {
			count++;
		}
		i++;
	}
	if(count==0) printf("prime number");
	else printf("not prime number");

//14.Write a program to print the first N Fibonacci numbers using a while loop.
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


//15. Write a program to calculate the power of a number (x^y) using a while loop.
	int x,y,i=1,result=1;
	printf("Enter Number:");
	scanf("%d",&x);
	printf("Enter Power:");
	scanf("%d",&y);
	while(i <= y) {
		result *= x;
		i++;
	}
	printf("%d^%d :%d",x,y,result);


	return 0;
}