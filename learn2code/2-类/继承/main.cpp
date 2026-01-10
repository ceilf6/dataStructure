// 把基类指针强制转换为派生类指针
#include <iostream>
// #include <iomanip.h>
#include "POINT.H"
#include "CIRCLE.H"
int main()
{
    Point *pointPtr, p(3.5, 5.3);
    Circle *circlePtr, c(2.7, 1.2, 8.9);
    cout << "Point p:" << p << "\nCircle c:" << c << endl;
    // Circle的对象还是作为Circle对象处理，但是用了一些类型转换
    pointPtr = &c;                  // 把Circle对象的地址赋给pointPtr
    circlePtr = (Circle *)pointPtr; // 把基类指针转换为派生类指针
    cout << "\nArea of c (via circlePtr):"
         << circlePtr->area() << endl;
    // 危险：把Point的对象作为Circle对象处理
    pointPtr = &p;                  // 把Point对象的地址赋给pointPtr
    circlePtr = (Circle *)pointPtr; // 把基类指针转换为派生类指针
    cout << "/nRadius of object circlePtr points to:" << circlePtr->getRadius() << endl;
    return 0;
}
