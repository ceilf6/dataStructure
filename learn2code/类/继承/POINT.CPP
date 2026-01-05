// POINT.CPP
#include <iostream>
#include "POINT.H"
Point::Point(float a, float b)
{
    x = a;
    y = b;
}
void Point::setPoint(float a, float b)
{
    x = a;
    y = b;
}
ostream &operator<<(ostream &output, const Point &p)
{
    output << '[' << p.x << ", " << p.y << ']';
    return output; // 使得能够连续调用
}
