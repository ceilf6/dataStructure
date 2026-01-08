#include <stdio.h>

int main()
{
    int a = -9;
    int b = a % 10;
    int a2 = a / 10;
    int a3 = 9 / 10; // 取整
    printf("%d,%d,%d,%d", a2, a3, b);

    return 0;
}