#include "stack.h"

template <class ElemType>
SeqStack<ElemType>::SeqStack(int size)
// 操作结果：申请内存、构造一个最大容量为size的空栈
{
    maxSize = size;
    if (elems != NULL)
        delete[] elems;
    elems = new ElemType[maxSize];
    top = -1;
}

template <class ElemType>
SeqStack<ElemType>::~SeqStack()
// 销毁栈: 清除管理的元素
{
    delete[] elems;
}

template <class ElemType>
int SeqStack<ElemType>::GetLength() const
// 操作结果：返回栈中元素个数
{
    return top + 1;
}

template <class ElemType>
bool SeqStack<ElemType>::IsEmpty() const
// 操作结果：如栈为空，则返回true，否则返回false
{
    return top == -1;
}

// 清空: 直接 top 指 -1 即可
template <class ElemType>
void SeqStack<ElemType>::Clear()
{
    top = -1;
}

// 添加元素
template <class ElemType>
SeqStack<ElemType>::Status SeqStack<ElemType>::Push(const ElemType e)
{
    if (top == maxSize - 1) // 栈已满
        return OVER_FLOW;
    else
    {
        elems[++top] = e; // ++top: top先加 1
        return SUCCESS;
    }
}

// 查询栈顶元素
template <class ElemType>
SeqStack<ElemType>::Status SeqStack<ElemType>::Top(ElemType &e) const
{
    if (IsEmpty()) // 栈空
        return UNDER_FLOW;
    else
    {
        e = elems[top]; // 用e返回栈顶元素
        return SUCCESS; // 栈非空,操作成功
    }
}

// 弹栈
template <class ElemType>
SeqStack<ElemType>::Status SeqStack<ElemType>::Pop(ElemType &e)
{
    if (IsEmpty()) // 栈空
        return UNDER_FLOW;
    else
    {
        e = elems[top--]; // top--: 先弹再减
        return SUCCESS;   // 操作成功
    }
}

// 遍历并作用函数
template <class ElemType>
void SeqStack<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
{
    for (int i = top; i >= 0; i--)
        (*Visit)(elems[i]);
}
