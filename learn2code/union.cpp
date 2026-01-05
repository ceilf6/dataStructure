#include <iostream>

union U
{
    int i;
    double d;
};

int main()
{
    U u;
    u.i = 10;
    // 此时只能安全使用 u.i

    printf("i: %d;d: %f\n", u.i, u.d);

    u.d = 3.14;
    // 此时 u.i 的值已经“被覆盖”

    printf("i: %d;d: %f\n", u.i, u.d);
    return 0;
}