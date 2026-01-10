#include "triple.h"
#include "Status.h"

// 通过指针来找到下一个非零元素
template <class ElemType>
struct CrossNode
{
    // 数据成员:
    Triple<ElemType> triElem;          // 三元组
    CrossNode<ElemType> *right, *down; // 同一行下一个非零 和 同一列下一个非零
    // 构造函数:
    CrossNode();
    CrossNode(const Triple<ElemType> &e,
              CrossNode<ElemType> *rLink = NULL,
              CrossNode<ElemType> *dLink = NULL);
};

template <class ElemType>
class CrossList
{
protected:
    CrossNode<ElemType> **rowHead, **colHead; // 行列链表头数组
    int rows, cols, num;                      // 稀疏矩阵的行数,列数及非零元个数
public:
    CrossList(int rs = DEFAULT_SIZE, int cs = DEFAULT_SIZE);
    // 构造一个rs行cs列的空稀疏矩阵
    ~CrossList();                         // 析构函数
    void Clear();                         // 清空稀疏矩阵
    int GetRows() const { return rows; }; // 返回稀疏矩阵行数
    int GetCols() const { return cols; }; // 返回稀疏矩阵列数
    int GetNum() const { return num; };   // 返回稀疏矩阵非零元个数
    Status SetElem(int r, int c, const ElemType &v);
    // 设置指定位置的元素值
    Status GetElem(int r, int c, ElemType &v); // 取指定位置的元素值
    CrossList(const CrossList<ElemType> &b);   // 复制构造函数
    CrossList<ElemType> &operator=(const CrossList<ElemType> &b);
    // 重载赋值运算符
    CrossList<ElemType> operator+(const CrossList<ElemType> &b);
    // 重载加法运算符
};
