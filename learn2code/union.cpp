#include <iostream>

union U
{
    int i;
    double d;
};

enum Type
{
    INT,
    DOUBLE
};

struct Value
{
    Type type;
    union
    {
        int i;
        double d;
    };
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

    Value v;
    v.type = INT;
    v.i = 10;

    if (v.type == INT)
    {
        std::cout << v.i;
    }

    return 0;
}