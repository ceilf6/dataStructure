#include <stdio.h>
int main()
{
    int a = 1;
    float b = 2.0;
    float c = a + b;
    printf("%f\n", c);
    printf("%d\n", c);

    float d = 100.00;
    printf("%d\n", d);

    int e = 1.00;
    float f = 1;
    printf("%f", f);
    return 0;
}