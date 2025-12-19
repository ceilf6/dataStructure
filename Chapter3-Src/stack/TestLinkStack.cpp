#include "LinkStack.h"

// 十进制转二进制函数
void DecimalToBinary(int decimal)
{
    LinkStack<int> s; // 创建一个整型栈

    cout << "将十进制数 " << decimal << " 转换为二进制数的过程：" << endl;
    cout << "----------------------------------------" << endl;

    // 特殊情况：0
    if (decimal == 0)
    {
        cout << "二进制结果：0" << endl;
        return;
    }

    // 转换过程
    int num = decimal;
    while (num > 0)
    {
        int remainder = num % 2; // 求余数
        s.Push(remainder);       // 余数入栈
        cout << num << " ÷ 2 = " << num / 2 << " ... 余数 " << remainder << " (入栈)" << endl;
        num = num / 2; // 继续除以2
    }

    cout << "----------------------------------------" << endl;
    cout << "二进制结果（从栈中依次弹出）：";

    // 依次出栈得到二进制数
    int bit;
    while (!s.IsEmpty())
    {
        s.Pop(bit);
        cout << bit;
    }
    cout << endl;
}

int main()
{
    cout << "============================================" << endl;
    cout << "    带头结点的链栈实现十进制转二进制" << endl;
    cout << "============================================" << endl;
    cout << endl;

    // 测试十进制59转二进制
    DecimalToBinary(59);

    cout << endl;
    cout << "----------------------------------------" << endl;
    cout << "验证：59 的二进制应该是 111011" << endl;
    cout << "计算：32 + 16 + 8 + 2 + 1 = 59" << endl;
    cout << "        2^5 + 2^4 + 2^3 + 2^1 + 2^0" << endl;
    cout << "----------------------------------------" << endl;

    cout << endl;
    cout << "其他测试用例：" << endl;
    cout << endl;

    // 测试其他数字
    DecimalToBinary(0);
    cout << endl;

    DecimalToBinary(1);
    cout << endl;

    DecimalToBinary(10);
    cout << endl;

    DecimalToBinary(255);
    cout << endl;

    // 测试栈的基本操作
    cout << "============================================" << endl;
    cout << "    测试栈的基本操作" << endl;
    cout << "============================================" << endl;

    LinkStack<int> testStack;

    cout << "1. 创建空栈，栈是否为空：" << (testStack.IsEmpty() ? "是" : "否") << endl;
    cout << "2. 依次压入元素：5, 10, 15, 20" << endl;

    testStack.Push(5);
    testStack.Push(10);
    testStack.Push(15);
    testStack.Push(20);

    cout << "3. 栈的长度：" << testStack.GetLength() << endl;

    int topElem;
    testStack.GetTop(topElem);
    cout << "4. 栈顶元素：" << topElem << endl;

    cout << "5. 遍历栈（从栈底到栈顶）：";
    testStack.Traverse(Write<int>);
    cout << endl;

    cout << "6. 依次弹出元素：";
    while (!testStack.IsEmpty())
    {
        int elem;
        testStack.Pop(elem);
        cout << elem << " ";
    }
    cout << endl;

    cout << "7. 弹出后栈是否为空：" << (testStack.IsEmpty() ? "是" : "否") << endl;

    return 0;
}
