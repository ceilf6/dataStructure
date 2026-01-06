#include "link-stack.h"
#include "Status.h"

// 构造
template <class ElemType>
LinkStack<ElemType>::LinkStack()
{
    top = NULL;
}

// 析构：处理管理的节点
template <class ElemType>
LinkStack<ElemType>::~LinkStack()
{
    Clear();
}

template <class ElemType>
int LinkStack<ElemType>::GetLength() const
// 遍历，返回栈中元素个数
{
    int count = 0; // 计数器
    Node<ElemType> *p;
    for (p = top; p != NULL; p = p->next)
        count++; // 统计链栈中结点数
    return count;
}

// 链式栈判断是否为空只需要判断栈顶指针是否为空
template <class ElemType>
bool LinkStack<ElemType>::IsEmpty() const
{
    return top == NULL;
}

// 遍历清除
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

// 返回栈顶元素前先判断是否栈空防止虚空索引
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

// 链式：弹栈后记得删除结点
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
