#include <string>
#include <iostream>

int priority(char op)
{
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

/*
1. 是数字/变量:
    直接输出
2. 运算符OP:
    while(栈非空 && 栈顶运算符优先级大于等于OP) 弹栈
    OP入栈
3. ( :
    直接入栈
4. ) :
    弹栈直到遇到 (

最后全部弹栈
*/
std::string mid2back(std::string str)
{
    std::string ans;
    char stack[100];
    int top = -1; // 栈顶

    for (char i : str) // C++用的不是of而是:
    {
        if (priority(i) == 0 && i != '(' && i != ')')
            ans += i;
        else if (priority(i) > 0)
        {
            while (top >= 0 && priority(stack[top]) >= priority(i))
            {
                ans += stack[top];
            }
            stack[++top] = i;
        }
        else if (i == '(')
        {
            stack[++top] = i;
        }
        else if (i == ')')
        {
            while (top >= 0 && stack[top] != '(')
            {
                ans += stack[top--];
            }
            if (top >= 0)
                top--;
        }
    }

    while (top >= 0)
        ans += stack[top--];

    return ans;
}

int main()
{
    std::string strEx[] = {
        "a+b",
        "a+b*c",
        "(a+b)*c",     // ab+c*
        "(a+(b-c))*d", // abc-+d*
        "(a)",
        "a",
        "(a+b)*(c-d/e)", // ab+cde/-*
    };
    for (std::string s : strEx)
    {
        const std::string strOut = mid2back(s);
        // printf("%s\n", strOut.c_str()); // %s 要求的是 char*, 所以得 c_str()
        std::cout << strOut << std::endl;
    }

    return 0;
}