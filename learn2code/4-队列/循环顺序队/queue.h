#include "Status.h"

/*
循环队列的引入是为了解决非循环顺序队列的假溢出问题
非循环队列判断溢出的条件是
    rear == maxSize -1
但是 实际上可能前面已经出队了一些元素，这部分空间没有利用起来
*/

template <class ElemType>
class SeqQueue
{
protected:
    int front, rear; // 队头队尾指针
    int maxSize;     // 队列容量
    ElemType *elems; // 元素存储空间
public:
    SeqQueue(int size = DEFAULT_SIZE);
    virtual ~SeqQueue();
    int GetLength() const;
    bool IsEmpty() const;
    void Clear();
    Status DelQueue(ElemType &e);
    Status GetHead(ElemType &e) const;
    Status EnQueue(const ElemType e);
    void Traverse(void (*visit)(const ElemType &)) const;
};

/*
另一种管理方式：本质其实就是 length = (rear-length+maxSize)%maxSize

template<class ElemType>
class SeqQueue {
protected:
    int front, length; // 队头指针，队列长度
    int maxSize; // 队列容量
    ElemType *elems; // 元素存储空间

- 用 front 和 length 表示队头位置和队列长度则入队操作为
    elem[front+length++] = e
    [] 语法糖会先取 front 位置然后再加 length 的size
*/