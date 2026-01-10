#include "线性表.h"
#include <cassert>
// template <class 和 template <typename 等价，现在更推荐 typename

// 1. 构造空顺序表
template <class ElemType>
SeqList<ElemType>::SeqList(int size)
{
    elems = new ElemType[size];
    assert(elems); // 防御式编程 - 断言宏 ，若条件表达式即分配的内存为空则终止程序
    maxLength = size;
    length = 0;
}

// 2. 以数组内容构造顺序表
template <class ElemType>
SeqList<ElemType>::SeqList(ElemType v[], int n, int size)
{
    elems = new ElemType[size];
    assert(elems);
    maxLength = size;
    length = n;
    for (int i = 0; i < length; i++)
        elems[i] = v[i];
}

// 3. 析构函数 - 需要对管理的元素们进行销毁
template <class ElemType>
SeqList<ElemType>::~SeqList()
{
    delete[] elems;
}

// 4. 清空顺序表 - 直接将表长干到 0
template <class ElemType>
void SeqList<ElemType>::Clear()
{
    length = 0;
}

// 5. 遍历顺序表元素并处理
template <class ElemType>
void SeqList<ElemType>::Traverse(void (*visit)(const ElemType &)) const
{
    // visit是函数指针，接受一个对单个进行处理的函数
    // *visit 解引用、取值，拿到函数然后传入当前元素
    for (int i = 1; i <= length; i++)
        (*visit)(elems[i - 1]);
}

// 6. 定位元素
template <class ElemType>
int SeqList<ElemType>::LocateElem(const ElemType &e) const
{
    int i = 0;
    while (i < length && elems[i] != e)
        i++;
    return i < length ? i + 1 : 0;
}

// 7. 取指定元素的值
template <class ElemType>
typename SeqList<ElemType>::Status SeqList<ElemType>::GetElem(int i, ElemType &e) const
{
    // Status 定义过了直接从空间里面拿，否则会报错
    if (i < 1 || i > length)
        return NOT_PRESENT;
    else
    {
        e = elems[i - 1];
        return ENTRY_FOUND;
    }
}

// 8. 修改元素的值
template <class ElemType>
typename SeqList<ElemType>::Status SeqList<ElemType>::SetElem(int i, const ElemType &e)
{
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        elems[i - 1] = e;
        return SUCCESS;
    }
}

// 9. 删除指定元素 - 后面填上来
template <class ElemType>
typename SeqList<ElemType>::Status SeqList<ElemType>::DeleteElem(int i, ElemType &e)
{
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        e = elems[i - 1];
        for (int j = i; j < length; j++)
            elems[j - 1] = elems[j];
        length--;
        // 别忘记减1长
        return SUCCESS;
    }
}

// 10. 在任意位置插入元素 - 后移留出位置
template <class ElemType>
typename SeqList<ElemType>::Status SeqList<ElemType>::InsertElem(int i, const ElemType &e)
{
    if (length == maxLength) // 是否超过最大长
        return OVER_FLOW;
    else if (i < 1 || i > length + 1)
        return RANGE_ERROR;
    else
    {
        for (int j = length; j >= i; j--)
            elems[j] = elems[j - 1];
        elems[i - 1] = e;
        length++;
        return SUCCESS;
    }
}

// 11. 在表尾插入元素
template <class ElemType>
typename SeqList<ElemType>::Status SeqList<ElemType>::InsertElem(const ElemType &e)
{
    if (length == maxLength)
        return OVER_FLOW;
    else
    {
        elems[length] = e;
        length++;
        return SUCCESS;
    }
}

// 12. 判断是否为空
template <class ElemType>
bool SeqList<ElemType>::IsEmpty() const
{
    return length == 0;
}
