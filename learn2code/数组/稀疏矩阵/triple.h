template <class ElemType>
struct Triple
{
    // 数据成员:
    int row, col;   // 非零元素的行下标与列下标
    ElemType value; // 非零元素的值
                    // 构造函数:
    Triple() {};
    Triple(int r, int c, ElemType v);
};