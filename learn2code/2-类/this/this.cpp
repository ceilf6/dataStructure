#include <iostream>

using namespace std;

class UsingThis
{
public:
    UsingThis(int = 99);
    void print() const;

private:
    int y;
};
UsingThis::UsingThis(int a) { y = a; } // 构造函数
void UsingThis::print() const
{
    cout << "y =" << y << "\n this->y =" << this->y << "\n(*this).y =" << (*this).y << '\n';
}

int main()
{
    UsingThis u(88);
    u.print();
    return 0;
}
