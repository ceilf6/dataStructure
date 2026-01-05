#include <iostream>
#include "time.h"

using namespace std;

main()
{
    Time t; // 类Time的实例对象t
    cout <<“The initial standard time is “;
    t.printStandardTime();
    t.setTime(14, 25, 9);
    cout <<“\n standard time after setTime is“;
    t.printStandardTime();
    t.setTime(70, 70, 70); // 试图设定非法值
    cout <<”\n After attempting invalid settings standard time is ”;
    t.printStandardTime();
    cout << endl;
    return 0;
}
