#include "单链表.h"

class String
{
protected:
    char *sVal; // 串值
    int length; // 串长
public:
    String();                              // 构造函数
    virtual ~String();                     // 析构函数
    String(const String &s);               // 复制构造函数
    String(const char *s);                 // 转换构造函数
    String(LinkList<char> &s);             // 线性表转换的构造函数
    int GetLength() const;                 // 求串长度
    bool IsEmpty() const;                  // 判断串是否为空
    String &operator=(const String &s);    // 赋值语句重载
    const char *CStr() const;              // 将串转换成字符数组
    char &String::operator[](int p) const; // 重载下标运算符
};

// 类中自带 this 所以要么去掉 s1 要么在全局声明
String operator+(const String &s1, const String &s2);
// 重载连接运算符+
bool operator==(const String &s1, const String &s2);
// 重载关系运算符==
bool operator<(const String &s1, const String &s2);
// 重载关系运算符<
bool operator>(const String &s1, const String &s2);
// 重载关系运算符>
bool operator<=(const String &s1, const String &s2);
// 重载关系运算符<=
bool operator>=(const String &s1, const String &s2);
// 重载关系运算符>=
bool operator!=(const String &s1, const String &s2);
// 重载关系运算符!=
