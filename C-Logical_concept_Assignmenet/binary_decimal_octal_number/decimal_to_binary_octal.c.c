#include <stdio.h>
//Write a C program to convert a decimal number into either binary or octal form based on user choice ('b' for binary, 'o' for octal).

int main() {
	int n, mod, result = 0, place = 1;
	char option;

	printf("Enter a decimal number: ");
	scanf("%d", &n);

	printf("'b' for Binary or 'o' for Octal: ");
	scanf(" %c", &option);

	int num = n;

	if (option == 'b') {
		while (num > 0) {
			mod = num % 2;
			result = result + mod* place;
			place = place * 10;
			num = num / 2;
		}
		printf("Binary of %d = %d\n", n, result);
	}
	else if (option == 'o') {

		while (num > 0) {
			mod = num % 8;
			result = result + mod * place;
			place = place * 10;
			num = num / 8;
		}
		printf("Octal of %d = %d\n", n, result);
	}
	else {
		printf("Invalid option Please  'b' or 'o'.\n");
	}

	return 0;
}