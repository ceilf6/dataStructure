// 单向递归：虽然可能DFS内部多次DFS，但是互不影响
// 直接多变量统计，相当于多个尾递归

long Fib(int n)
{
    if (n == 0 || n == 1)
        return n; // 递归出口
    else
        return Fib(n - 1) + Fib(n - 2); // 递归调用
}

long Fib(int n)
{
    if (n == 0 || n == 1)
        return n;
    long twoback = 0, oneback = 1, current;
    for (int i = 2; i <= n; i++)
    {
        current = twoback + oneback;
        twoback = oneback;
        oneback = current;
    }
    return current;
}
