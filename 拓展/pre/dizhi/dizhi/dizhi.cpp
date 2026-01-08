#include <stdio.h>
int main()
{
    int a = 10;
    int*b = &a;     // 注意指针的声明需要在类型后加*号；&：取对应变量值的地址
    *b = 100;        //*号后加变量名：取变量名对应地址的值
    printf("%d", a); //*b改变了a内存的值
    return 0;
}