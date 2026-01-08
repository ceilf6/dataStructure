#include <stdio.h>
#include <time.h>

int main()
{
    time_t t;
    time(&t);
    struct tm *t2;
    t2 = localtime(&t);
    printf("%s", ctime(&t));
    return 0;
}

/*`time`函数和`localtime`函数都是用于处理时间的C标准库函数，但它们的作用和用法略有不同：

1. **time函数：**
   - `time`函数用于获取当前的系统时间，返回的是一个 `time_t` 类型的值，表示从某个特定起点（通常是1970年1月1日UTC时间，也称为Epoch时间）到当前时间所经过的秒数。
   - 它不考虑时区和本地时间，返回的时间是以秒为单位的相对时间，通常用于记录事件发生的时间或计算时间间隔。

2. **localtime函数：**
   - `localtime`函数用于将 `time_t` 类型的时间转换为本地时间，并返回一个指向 `struct tm` 结构体的指针，该结构体包含了年、月、日、时、分、秒等时间信息。
   - 它会考虑系统的时区设置，将 `time_t` 类型的时间转换为对应时区的本地时间。

总的来说，`time`函数用于获取当前的系统时间，而`localtime`函数用于将 `time_t` 类型的时间转换为本地时间。*/