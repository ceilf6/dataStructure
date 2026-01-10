#include "重载运算符-简化字符串操作.h"

// 时间复杂度(主串长n,模式串长m): O((n-m+1)*m)

int BF_find(const String &ob, const String &pat, const int p = 0)
{
    int i = p, j = 0;
    while (i < ob.GetLength() && j < pat.GetLength() && pat.GetLength() - j <= ob.GetLength() - i)
        if (ob[i] == pat[j])
        { // 继续比较后续字符
            i++;
            j++;
        }
        else
        { // 指针回退,重新开始新的匹配
            i = i - j + 1;
            j = 0;
        }
    if (j >= pat.GetLength())
        return i - j; // 匹配成功
    else
        return -1; // 匹配失败
}
