#include <iostream>
#include "工具函数.h"
#include "重载运算符-简化字符串操作.h"

using namespace std;

void Write(const String &str)
{
    cout << str.CStr() << endl; // 输出串值
}

void Copy(String &s1, const String &s2)
{
    const char *cs2 = s2.CStr();           // 初始串，通过 cs2 常量只读视图确保 s2 的安全
    char *cs1 = new char[strlen(cs2) + 1]; // 临时缓冲区
    strcpy(cs1, cs2);                      // 复制串
    s1 = cs1;                              // 串赋值、利用 = 重载
    delete[] cs1;                          // 释放临时空间
}

void Copyn(String &s1, const String &s2, int n)
{
    const char *cs2 = s2.CStr();                 // 初始串
    int len = strlen(cs2) < n ? strlen(cs2) : n; // 取目标串长
    char *cs1 = new char[len + 1];               // 申请临时空间
    strncpy(cs1, cs2, n);                        // 复制串
    cs1[len] = '\0';                             // 串值以'\0'结束
    s1 = cs1;                                    // 串赋值
}

Status Insert(String &s1, const String &s2, int p)
{
    const char *cs1 = s1.CStr(); // 取第一个串
    const char *cs2 = s2.CStr(); // 取第二个串
    if (p >= 0 && p < strlen(cs1))
    {
        int len = strlen(cs1) + strlen(cs2);
        char *cs = new char[len + 1]; // 申请临时空间
        strncpy(cs, cs1, p);          // 复制第一个串前部分的串值	       	    cs[p] = '\0';
        strcat(cs, cs2);              // 连接第二个串
        int j = p + strlen(cs2);
        for (int i = p; i < strlen(cs1); i++, j++)
            cs[j] = cs1[i]; // 复制第一个串后部分的串值
        cs[len] = '\0';
        s1 = cs; // 串赋值
        return SUCCESS;
    }
    return RANGE_ERROR;
}

// 删除从 p 开始的 n 个字符
Status Delete(String &s, int p, int n)
{
    const char *cs = s.CStr(); // 取原串值
    if (p >= 0 && (p + n) < strlen(cs))
    {
        int len = strlen(cs) - n;       // 求新串的长度
        char *news = new char[len + 1]; // 申请临时空间
        strncpy(news, cs, p);           // 复制原串前部分的串值
        int j = p + n;
        for (int i = p; i < len; i++, j++)
            news[i] = cs[j];
        // 复制第一个串后部分的串值
        news[len] = '\0';
        s = news;      // 串赋值
        delete[] news; // 释放临时空间
        return SUCCESS;
    }
    return RANGE_ERROR;
}

// 子串：从 p 开始的 n 个字符
String SubString(const String &s, int p, int n)
{
    if (0 <= p && p + n < s.GetLength() && 0 <= n) // PPT上写的 s.length 错了，因为这是 protected ，得通过暴露函数拿
    {
        char *sub = new char[n + 1]; // 申请临时空间
        const char *strp = s.CStr(); // 生成字符数组
        strncpy(sub, strp + p, n);   // 复制串
        sub[n] = '\0';               // 串值以'\0'结束
        String cs(sub);              // 生成串对象
        delete[] sub;                // 释放临时空间
        return cs;
    }
    else
    {                  // 返回空串
        String cs(""); // 生成空串对象
        return cs;
    }
}
