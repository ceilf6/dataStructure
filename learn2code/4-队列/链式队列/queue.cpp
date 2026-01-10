#include "queue.h"

// 构造初始化
template <class ElemType>
LinkQueue<ElemType>::LinkQueue()
{
    rear = front = new Node<ElemType>;
}

// 析构：在清除元素的同时别忘记最后清理头指针，因为 Clear 只清理了虚拟队头节点后面的元素
template <class ElemType>
LinkQueue<ElemType>::~LinkQueue()
{
    Clear();
    delete front;
}

// 遍历求长度
template <class ElemType>
int LinkQueue<ElemType>::GetLength() const
{
    int count = 0;
    Node<ElemType> *p;
    for (p = front->next; p != NULL; p = p->next)
        count++;
    return count;
}

// 和顺序队一样判断是否空直接判断双指针是否在一处
template <class ElemType>
bool LinkQueue<ElemType>::IsEmpty() const
{
    return rear == front;
}

template <class ElemType>
void LinkQueue<ElemType>::Clear()
{
    Node<ElemType> *p = front->next;
    while (p != NULL)
    {
        front->next = p->next;
        delete p;
        p = front->next;
    }
    rear = front;
}

template <class ElemType>
Status LinkQueue<ElemType>::EnQueue(const ElemType e)
{
    Node<ElemType> *p;
    p = new Node<ElemType>(e);
    if (p) // 开创成功
    {
        rear->next = p;    // 队尾指向新节点
        rear = rear->next; // 队尾到新节点
        return SUCCESS;
    }
    else
        return OVER_FLOW;
}

// 队头：front虚拟头的下一个
template <class ElemType>
Status LinkQueue<ElemType>::GetHead(ElemType &e) const
{
    if (!IsEmpty())
    {
        e = front->next->data;
        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}

template <class ElemType>
Status LinkQueue<ElemType>::DelQueue(ElemType &e)
{
    if (!IsEmpty())
    {
        Node<ElemType> *p = front->next;
        e = p->data;           // 取头存储到 e 地址
        front->next = p->next; // 队头指针指向新的头，也就是第二个节点
        if (rear == p)         // 如果没有第二个节点，那么rear所在的第一个点届时会被抛弃，所以得跟上front
            rear = front;
        delete p;
        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}

template <class ElemType>
void LinkQueue<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
{
    Node<ElemType> *p;
    for (p = front->next; p != NULL; p = p->next)
        (*Visit)(p->data);
}
