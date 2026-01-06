#include "重载运算符-简化字符串操作.h"
#include <iostream>

String::String()
{
    length = 0;     // 串长度为0
    sVal = nullptr; // 空串
}

String::~String()
{
    delete[] sVal; // 释放串的存储空间sVal
}

String::String(const String &s) // s 是 String 类型，但是 strlen,strcpy 等是C的函数不认识 String
// 所以需要 .CStr() 转换为 char*
{
    length = strlen(s.CStr());   // 设置串长
    sVal = new char[length + 1]; // 分配存储空间
    strcpy(sVal, s.CStr());      // 复制串值
    // String.CStr() 拿到的字符串已经以 '\0' 结尾了
}

String::String(const char *s)
{
    length = strlen(s);          // 设置串长
    sVal = new char[length + 1]; // 分配存储空间
    strcpy(sVal, s);             // 复制串值
    sVal[length] = '\0';
}

String::String(LinkList<char> &s)
{
    length = s.GetLength();          // 串长
    sVal = new char[length + 1];     // 分配存储空间
    for (int i = 0; i < length; i++) // 复制串值
        s.GetElem(i + 1, sVal[i]);
    // 遍历拿值并存储到 char[] 对应位置中
    sVal[length] = '\0'; // 串值以'\0'结束
}

int String::GetLength() const
{
    return length;
}

bool String::IsEmpty() const
{
    return length == 0;
}

String &String::operator=(const String &s)
{
    if (&s != this)
    {
        delete[] sVal;               // 释放原串存储空间
        length = strlen(s.CStr());   // 设置串长
        sVal = new char[length + 1]; // 分配存储空间
        strcpy(sVal, s.CStr());      // 复制串值
    }
    return *this;
}

const char *String::CStr() const
{
    return (const char *)sVal; // 串值类型转换
}

char &String::operator[](int p) const
{
    return sVal[p];
}

String operator+(const String &s1, const String &s2)
{
    const char *cs1 = s1.CStr(); // 取第一个串值
    const char *cs2 = s2.CStr(); // 取第二个串值
    char *cs = new char[strlen(cs1) + strlen(cs2) + 1];
    strcpy(cs, cs1); // 复制第一个串
    strcat(cs, cs2); // 连接第二个串
    String s(cs);    // 定义串对象并初始化
    delete[] cs;     // 释放临时空间
    return s;
}

bool operator==(const String &s1, const String &s2)
{
    return strcmp(s1.CStr(), s2.CStr()) == 0;
}

bool operator<(const String &s1, const String &s2)
{
    return strcmp(s1.CStr(), s2.CStr()) < 0;
}

bool operator>(const String &s1, const String &s2)
{
    return strcmp(s1.CStr(), s2.CStr()) > 0;
}

bool operator<=(const String &s1, const String &s2)
{
    return strcmp(s1.CStr(), s2.CStr()) <= 0;
}

bool operator>=(const String &s1, const String &s2)
{
    return strcmp(s1.CStr(), s2.CStr()) >= 0;
}

bool operator!=(const String &s1, const String &s2)
{
    return strcmp(s1.CStr(), s2.CStr()) != 0;
}
