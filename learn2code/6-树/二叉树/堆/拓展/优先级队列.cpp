#include "优先级队列.h"

// 构造函数
template <class T>
PriorityQueue<T>::PriorityQueue(int cap)
{
    capacity = cap;
    size = 0;
    data = new T[capacity];
}

// 析构函数
template <class T>
PriorityQueue<T>::~PriorityQueue()
{
    delete[] data;
}

// 判空
template <class T>
bool PriorityQueue<T>::IsEmpty() const
{
    return size == 0;
}

// 判满
template <class T>
bool PriorityQueue<T>::IsFull() const
{
    return size == capacity;
}

// 入队
template <class T>
void PriorityQueue<T>::Push(const T &x)
{
    if (IsFull())
        return;

    data[size] = x;
    FilterUp(size);
    size++;
}

// 出队（删除堆顶）
template <class T>
void PriorityQueue<T>::Pop()
{
    if (IsEmpty())
        return;

    data[0] = data[size - 1];
    size--;
    FilterDown(0);
}

// 访问堆顶
template <class T>
T PriorityQueue<T>::Top() const
{
    if (IsEmpty())
        throw "PriorityQueue is empty";
    return data[0];
}

// 向上调整（最小堆）
template <class T>
void PriorityQueue<T>::FilterUp(int index)
{
    int parent;
    T temp = data[index];

    while (index > 0)
    {
        parent = (index - 1) / 2;
        if (data[parent] <= temp)
            break;

        data[index] = data[parent];
        index = parent;
    }
    data[index] = temp;
}

// 向下调整（最小堆）
template <class T>
void PriorityQueue<T>::FilterDown(int index)
{
    int child;
    T temp = data[index];

    while (2 * index + 1 < size)
    {
        child = 2 * index + 1;

        if (child + 1 < size && data[child + 1] < data[child])
            child++;

        if (data[child] >= temp)
            break;

        data[index] = data[child];
        index = child;
    }
    data[index] = temp;
}
