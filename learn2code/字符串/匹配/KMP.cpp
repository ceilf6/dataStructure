/*
能走多远并不取决于顺境，而是在于逆境中能否迭代到曾经相同的自己                            ——KMP

一般的字符串匹配再碰到不匹配时会回退主串的指针，但是KMP算法可以利用历史匹配信息避免冗余计算

而且KMP可以适用于所有可切片比较的对象，不止字符串
————————————————
版权声明：本文为CSDN博主「ceilf6」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/2301_78856868/article/details/147013847
*/

// https://www.bilibili.com/video/BV1Er421K7kF 这个视频不错
// 前缀函数 p[i] 表示 第i个的最长匹配真前后缀长度（后缀而不需要反转）
/*
i:     0 1 2 3 4
S[i]:  a b a b a
p[i]:  0 0 1 2 3 // p[0]=0是因为需要真：不能等于字符串本身
*/
// 前缀函数中 p[x] = L目标 的就是找到了

#include "../重载运算符-简化字符串操作.h"

// 计算失配数组（前缀函数）
// f[j] 表示 pat[0..j-1] 的最长相等真前后缀长度
void GetFailure(const String &pat, int *f)
{
    int m = pat.GetLength();
    f[0] = -1; // 约定：第一个位置失配时，主串指针后移
    if (m == 1)
        return;

    f[1] = 0; // 单个字符不“真”
    int len = 0;
    for (int i = 2; i < m; i++)
    {
        while (len > 0 && pat[len] != pat[i - 1])
        {
            len = f[len]; // 如果不匹配：迭代到更短的前后缀
        }
        if (pat[len] == pat[i - 1])
        {
            len++;
        }
        f[i] = len;
    }
}

// KMP 匹配：在主串 ob 中从位置 p 开始查找模式串 pat
int KMP_find(const String &ob, const String &pat, int p = 0)
{
    int n = ob.GetLength();
    int m = pat.GetLength();
    if (m == 0)
        return p;
    if (n == 0 || m > n - p)
        return -1;

    int *f = new int[m];
    GetFailure(pat, f); // 拿到模式串的前缀函数

    int i = p, j = 0;
    while (i < n && j < m)
    {
        if (j == -1 || pat[j] == ob[i])
        {
            i++;
            j++;
        }
        else
        {
            j = f[j]; // 那么失败时，模式串根据前缀函数回退，主串不回退（从而实现复用）
        }
    }

    delete[] f;
    return (j == m) ? i - j : -1;
}
