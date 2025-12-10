#include <stdio.h>

int main()
{	// 1. Write a program to print the numbers from 1 to 10 using a while loop.

	for(int i=1; i<=10; i++) printf("%d ",i);

//2. Print the even numbers from 2 to 20 using a while loop.

	for(int i=2; i<=20; i++) {
		if(i%2==0) {
			printf("%d ",i);
		}
	}

//3. Write a program to print the odd numbers from 1 to 20 using a while loop.

	for(int i=1; i<=20; i++) {
		if(i%2!=0) {
			printf("%d ",i);
		}
	}

//4. Write a program to print all integers between 10 and 1 in reverse order using a while loop.

for(int i=10; i>=1; i--) printf("%d ",i);


//5. Write a program to print the numbers 1 to 100, but only print those that are divisible by 5.
	for(int i=1; i <=100; i++) {
		if(i%5==0) {
			printf("%d ",i);
		}
	}

//6. Write a program that computes the sum of integers from 1 to N, where N is provided by the user.

int main(){
    int n,sum=0;
    printf("Enter n:");
        scanf("%d",&n);
    for(int i=1;i<=n;i++){
        sum +=i;
        //printf(" %d ",sum);
    }
    printf("\n sum: %d ",sum); }

	return 0;

// 7. Write a program to compute the sum of all even numbers between 1 and 100.

int main()
{
	int sum=0;
	for(int i=1; i<=100; i++) {
		if(i%2==0) {  
		//if(i%2!=0) {  //if odd number chahiye the
		    printf("%d ",i);
			sum +=i;
		}
	}
	printf("%d ",sum);

// 8. Write a program to compute the sum of digits of a given number.

int main(){
    int n,sum=0,count =0;
    printf("Enter N:");
    scanf("%d",&n);
    for(int digit;n >=1;){
        count++;
        digit=n%10;
        sum +=digit;
        n/=10;
    }
    printf("%d ",sum);
    printf("\n %d",count);


// 9. Write a program to calculate the average of N numbers entered by the user.

int main(){
    int n,sum=0,count=0;
    printf("Enter N:");
    scanf("%d",&n);
    for(int digit;n >1;){
        count++;
        digit=n%10;
        sum +=digit;
        n/=10;
        
        
    }
    printf("avg:%d",sum/count);


// 10. Write a program that sums all the multiples of 7 between 1 and 500.

int main()
{
    int sum=0;
    for(int i=1;i<=500;i++){
        if(i%7==0){
            sum +=i;
        }
    }
    printf("sums all the multiples of 7 between 1 and 500 : %d",sum);

// Factorials and Mathematical Problems

// 11. Write a program to compute the factorial of a given number using a while loop.

int main()
{int n,factorial=1;
printf("Enter N:");
scanf("%d",&n);
for(int i=1;i<=n;i++){
    factorial *=i;
    
}

printf("%d",factorial);

// 12. Write a program to find the product of all odd numbers from 1 to N.

int main(){
    int n,prod=1;
    printf("Enter N:");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        if(i%2 !=0){
           // printf("%d ",i);
        prod *=i;}
    }
    printf("\n all odd prod : %d",prod);

// 13. Write a program to check whether a number is a prime number.

int main() {
	int n,count=0,loop=0;
	printf("Enter N :");
	scanf("%d",&n);
	for(int i=2; i*i<=n; i++) {
		loop++;
		if(n%i==0) {
			count++;
		}
	}
	printf("loop:%d",loop);
	if(count==0) printf("\nprime number");
	else printf("\nnot prime number");

// 14. Write a program to print the first N Fibonacci numbers using a while loop.

int main()
{
    int n,nxt;
    printf("Enter n:");
    scanf("%d",&n);
    for(int a=0,b=1,i=1;i <=n;i++){
        
       nxt=a+b;
        a=b;
        b=nxt;
        printf("%d ",nxt);

        //sewp method
        // a=a+b 
        // b =a-b 
        // a=a-b
         
    }

// 15. Write a program to calculate the power of a number (x^y) using a while loop.

int main()
{
    int x,y,result=1;
    printf("Enter X: ");
    scanf("%d",&x);
    printf("power y: ");
    scanf("%d",&y);
    for(int i=1;i<=y;i++){
        result *=x;
    }
    printf("%d ^ %d :%d",x,y,result);
}