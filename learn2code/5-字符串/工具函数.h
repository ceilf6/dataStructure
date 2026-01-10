#include "Status.h"

class String
{
protected:
    char *sVal; // 串值
    int length; // 串长
public:
    void Write(const String &s); // 输出串
    void Copy(String &s1, const String &s2);
    // 将串s2复制到串s1
    void Copy(String &s1, const String &s2, int n);
    // 将串s2复制n个字符到串s1
    Status Insert(String &s1, const String &s2, int p);
    // 将字符串s2插入到s1的p位置
    Status Delete(String &s, int p, int n);
    // 删除字符串s中从p位置开始长度为n的字符串
    String SubString(const String &s, int p, int n);
    // 求串s的第p个字符开始的长度为n的子串
};