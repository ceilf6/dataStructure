#include "queue.h"
#include "Status.h"

// 构造新队列
template <class ElemType>
SeqQueue<ElemType>::SeqQueue(int size)
{
    maxSize = size;
    if (elems != NULL)
        delete[] elems;
    elems = new ElemType[maxSize];
    rear = front = 0;
}

template <class ElemType>
SeqQueue<ElemType>::~SeqQueue()
{
    delete[] elems;
}

// 因为是循环队列所以注意得 +maxSize) % maxSize 轮转一下
template <class ElemType>
int SeqQueue<ElemType>::GetLength() const
{
    return (rear - front + maxSize) % maxSize;
}

// 判断是否为空直接判断队头队尾双指针是否一起
template <class ElemType>
bool SeqQueue<ElemType>::IsEmpty() const
{
    return rear == front;
}

// 清除的话直接两个指针移到一起即可
template <class ElemType>
void SeqQueue<ElemType>::Clear()
{
    rear = front = 0;
}

template <class ElemType>
Status SeqQueue<ElemType>::EnQueue(const ElemType e)
{
    if ((rear + 1) % maxSize == front) // 先判断是否满了
        return OVER_FLOW;
    else
    {
        elems[rear] = e;
        rear = (rear + 1) % maxSize;
        return SUCCESS;
    }
}

template <class ElemType>
Status SeqQueue<ElemType>::GetHead(ElemType &e) const
{
    if (!Empty()) // 读取前先判断是否空
    {
        e = elems[front];
        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}

// 队头出队
template <class ElemType>
Status SeqQueue<ElemType>::DelQueue(ElemType &e)
{
    if (!IsEmpty())
    {
        e = elems[front];
        front = (front + 1) % maxSize;
        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}

// 遍历并应用
template <class ElemType>
void SeqQueue<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
{
    for (int i = front; i != rear; i = (i + 1) % maxSize)
        (*Visit)(elems[i]);
}
