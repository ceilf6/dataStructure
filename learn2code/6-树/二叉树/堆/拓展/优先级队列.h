// 优先级队列 = 堆 + 对外封装接口

#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <iostream>

template <class T>
class PriorityQueue
{
private:
    T *data;      // 堆数组
    int capacity; // 最大容量
    int size;     // 当前元素个数

    void FilterUp(int index);   // 向上调整
    void FilterDown(int index); // 向下调整

public:
    PriorityQueue(int cap = 100);
    ~PriorityQueue();

    bool IsEmpty() const;
    bool IsFull() const;

    void Push(const T &x); // 入队
    void Pop();            // 出队（删除堆顶）
    T Top() const;         // 访问堆顶
};

#endif
