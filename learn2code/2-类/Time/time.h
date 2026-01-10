#ifndef TIME1_H
#define TIME1_H
class Time
{
public:
    Time();                      // 默认构造函数
    void setTime(int, int, int); // 设置时、分、秒
    void printStandardTime();    // 打印标准格式的时间
private:
    int hour;   // 0-23
    int minute; // 0-59
    int second; // 0-59
};
#endif
