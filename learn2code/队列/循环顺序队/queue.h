#include "Status.h"

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

*/