#include "link-stack.h"
#include "Status.h"

template <class ElemType>
LinkStack<ElemType>::LinkStack()
{
    top = NULL;
}

template <class ElemType>
LinkStack<ElemType>::~LinkStack()
{
    Clear();
}

template <class ElemType>
int LinkStack<ElemType>::GetLength() const
// 操作结果：返回栈中元素个数
{
    int count = 0; // 计数器
    Node<ElemType> *p;
    for (p = top; p != NULL; p = p->next)
        count++; // 统计链栈中结点数
    return count;
}

template <class ElemType>
bool LinkStack<ElemType>::IsEmpty() const
{
    return top == NULL;
}

template <class ElemType>
void LinkStack<ElemType>::Clear()
// 操作结果：清空栈
{
    Node<ElemType> *p;
    while (top != NULL)
    {
        p = top;
        top = top->next;
        delete p;
    }
}

template <class ElemType>
Status LinkStack<ElemType>::Push(const ElemType item)
{
    Node<ElemType> *p = new Node<ElemType>(item, top);
    if (p == NULL) // 系统内存耗尽
        return OVER_FLOW;
    else
    { // 操作成功
        top = p;
        return SUCCESS;
    }
}

template <class ElemType>
Status LinkStack<ElemType>::Top(ElemType &e) const
{
    if (IsEmpty()) // 栈空
        return UNDER_FLOW;
    else
    {
        e = top->data; // 用e返回栈顶元素
        return SUCCESS;
    }
}

template <class ElemType>
Status LinkStack<ElemType>::Pop(ElemType &e)
{
    if (IsEmpty()) // 栈空
        return UNDER_FLOW;
    else
    {                            // 操作成功
        Node<ElemType> *p = top; // 保留原栈顶
        e = top->data;           // 用e返回栈顶元素
        top = top->next;         // 修改栈顶
        delete p;                // 删除原栈顶结点
        return SUCCESS;
    }
}

template <class ElemType>
void LinkStack<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
// 从栈顶到栈底依次对栈的每个元素调用函数(*visit)访问
{
    Node<ElemType> *p;
    for (p = top; p != NULL; p = p->next)
        (*Visit)(p->data);
}
