#include <iostream>

int main()
{
    int x = 9;
    int &y = x;
    x = 13;
    printf("x: %d,y: %d", x, y);
    return 0;
}