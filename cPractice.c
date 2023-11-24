#include <stdio.h>

int main(){
    const float PI = 3.1415926;
    float r = 0.0;
    printf("Please input the radius of the circle: ");
    scanf("%f", &r);
    printf("The circumference of the circle is %f\n", 2 * PI * r);
    printf("The area of the circle is %f\n", PI * r * r);
    return 0;
}