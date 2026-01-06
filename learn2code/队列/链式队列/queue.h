#include "Status.h"

template <class ElemType>
class LinkQueue
{
protected:
    Node<ElemType> *front, *rear;
    // 注意链式队的头是虚拟头，第一个元素是 front->next
public:
    LinkQueue();
    virtual ~LinkQueue();
    int GetLength() const;
    bool IsEmpty() const;
    void Clear();
    Status DelQueue(ElemType &e);
    Status GetHead(ElemType &e) const;
    Status EnQueue(const ElemType e);
    void Traverse(void (*visit)(const ElemType &)) const;
};
