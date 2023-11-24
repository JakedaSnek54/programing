#include <stdio.h>
#include <ctype.h>

int main(){
    char operator;
    double firstNumber, secondNumber, result;
    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);
    printf("Enter two operands: ");
    scanf("%lf %lf", &firstNumber, &secondNumber);
    switch (operator)
    {
    case '+':
        result = firstNumber + secondNumber;
        break;
    case '-':
        result = firstNumber - secondNumber;
        break;
    case '*':
        result = firstNumber * secondNumber;
        break;
    case '/':
        result = firstNumber / secondNumber;
        break;
    default:
        printf("Error! operator is not correct");
        break;
    }
    printf("%.1lf %c %.1lf = %.1lf\n", firstNumber, operator, secondNumber, result);


    return 0;
}