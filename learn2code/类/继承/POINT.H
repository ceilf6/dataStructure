// POINT.H
#ifndef POINT_H
#define POINT_H
#include <iostream>

using namespace std;

class Point
{
    friend ostream &operator<<(ostream &, const Point &);

public:
    Point(float = 0, float = 0); // 默认的构造函数
    void setPoint(float, float); // 设置坐标值
    float getX() const { return x; }
    float getY() const { return y; }

protected:      // 允许派生类访问
    float x, y; // 点（类Point的对象）的x和y坐标
};
#endif
