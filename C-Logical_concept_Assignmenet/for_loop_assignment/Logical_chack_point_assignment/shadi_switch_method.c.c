#include <stdio.h>

int main() {
    char gender;
    int age;

    printf("Enter gender : ");  //(m for male, f for female)
    scanf(" %c", &gender);

    printf("Enter age: ");
    scanf("%d", &age);

    switch (gender) {
        case 'm':
        case 'M':
            if (age >= 21)
                printf("He can marry \n");
            else
                printf("Padhai likhai karo, IAS/YAS bano!\n");
            break;

        case 'f':
        case 'F':
            if (age >= 18)
                printf("She can marry \n");
            else
                printf("Choti bacchi ho kya? \n");
            break;

        default:
            printf("Invalid gender! \n");
    }

    return 0;
}