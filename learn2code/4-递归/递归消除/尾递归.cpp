// 尾递归：仅在DFS末尾调用DFS
// 尾递归消除直接用一个ans变量统计循环遍历即可

#include <iostream>

float f(int n)
{
    if (n < 0)
        printf("输入数据错误!");
    else if (n != 0)
        return (n * f(n - 1));
    else
        return (1.0);
}

long fact(int n)
{
    int product = 1;

    for (int i = 1; i <= n; i++)
        product = product * i;

    return product;
}
