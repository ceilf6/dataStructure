#include <stdio.h>

int global;

void while_(void)
{
    int a = 0;
    while (a <= 10)
    {
        if (a % 2 == 1) // c语言也是用两个等号表示判断
        {
            printf("%d\n", a);
            break;
        }
        a += 1;
    }
}

void for_()
{

    for (int b = 0; b += 1; b <= 10)
    // for的结构：（初始化；判断;操作）
    {
        if (b % 2 == 1)
        {
            printf("%d\n", b);
            break;
        }
    }
}

void Loop1(void)
{

    int a, min, max, t;
    printf("Type an Integer:");
    scanf("%d", &min);
    printf("Type an Integer:");
    scanf("%d", &max);
    /*    if (min > max)
        {
            t = min;
            min = max;
            max = t;
        }*/
    if (min > max)
    {
        max += min;
        min = max - min;
        max = max - min;
    }

    // for (int i = min; i <= max; i += 1 /*; i <= max*/)
    for (min; min <= max; min++)
    {
        printf("%d\n", /*i*/ min);
        global = min;
    }

    printf("%d\n", global); // i是局部变量，必须将他的值存到全局变量中才能在函数外输出
}

int main()
{
    // while_();
    // for_();
    Loop1();
    return 0;
}