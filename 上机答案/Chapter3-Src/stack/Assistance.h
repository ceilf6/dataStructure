#ifndef __ASSISTANCE_H__
#define __ASSISTANCE_H__

// 辅助软件包

// ANSI C++标准库头文件
#include <cstring>   // 标准串操作
#include <iostream>  // 标准流操作
#include <limits>    // 极限
#include <cmath>     // 数学函数
#include <fstream>   // 文件流操作
#include <cctype>    // 字符处理
#include <ctime>     // 时间和时间函数
#include <cstdlib>   // 标准库
#include <cstdio>    // 标准输入输出
#include <iomanip>   // 输入输出流格式设置
#include <cstdarg>   // 支持变长参数列表
#include <cassert>   // 支持断言
using namespace std; // 标准库函数命名空间std

// 自定义类型
enum Status
{
    SUCCESS,
    FAIL,
    UNDER_FLOW,
    OVER_FLOW,
    RANGE_ERROR,
    DUPLICATE_ERROR,
    NOT_PRESENT,
    ENTRY_INSERTED,
    ENTRY_FOUND,
    VISITED,
    UNVISITED
};

// 宏定义
#define DEFAULT_SIZE 1000        // 缺省元素个数
#define DEFAULT_INFINITY 1000000 // 缺省无穷大

// 辅助函数声明

template <class ElemType>
void Write(const ElemType &e); // 显示数据元素

// 辅助函数实现
template <class ElemType>
void Write(const ElemType &e)
// 操作结果：显示数据元素
{
    cout << e;
}

#endif
