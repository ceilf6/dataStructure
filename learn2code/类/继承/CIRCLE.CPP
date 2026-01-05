// 定义类Circle的成员函数
#include "CIRCLE.H"
#include <iomanip> // for setiosflags and setprecision
// 先用成员初始化值调用类Point的构造函数，
// 然后再调用类Circle的构造函数初始化半径值
Circle::Circle(float r, float a, float b)
    : Point(a, b) // 调用基类的构造函数
{
    radius = r;
}
// 设置圆的半径值
float Circle::getRadius() const { return radius; }
// 计算圆的面积
float Circle::area() const
{
    return 3.14159 * radius * radius;
}
// 以Center=[x, y]; Radius=#.## 形式输出一个圆
ostream &operator<<(ostream &output, const Circle &c)
{
    output << "Center=[" << c.x << ", " << c.y
           << "];Radius=" << setiosflags(ios::showpoint)
           << setprecision(2) << c.radius;
    return output; // 使得能够连续调用
}