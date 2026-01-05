// CIRCLE.H
#ifndef CIRCLE_H
#define CIRCLE_H
#include <iostream>
// #include <iomanimp>
#include "POINT.H"
class Circle : public Point // public 继承方式
{
    friend ostream &operator<<(ostream &, const Circle &);

public:
    Circle(float r = 0.0, float x = 0, float y = 0);
    void setRadius(float);   // 设置半径值
    float getRadius() const; // 返回半径值
    float area() const;      // 计算圆的面积
protected:
    float radius;
};
#endif