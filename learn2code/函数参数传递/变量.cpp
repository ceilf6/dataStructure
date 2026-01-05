#include <iostream>

// int change(int a2, int b2)
// {
//     a2 = 10; // 局部工作区
//     b2 = 20;
//     return a2;
// }

void change(int &a2, int &b2)
{
    a2 = 10;
    b2 = 20;
}

int main()
{
    int a = 1;
    int b = 2;
    change(a, b); // 引用传递仍然是变量名
    printf("a:%d,b:%d\n", a, b);
    // a = change(a, b);
    // printf("a:%d,b:%d\n", a, b);

    return 0;
}