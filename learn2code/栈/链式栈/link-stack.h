#include "node.h"
#include "Status.h"
// struct Node
// {

//     next
// };

template <class ElemType>
class LinkStack
{
protected:
    Node<ElemType> *top; // 栈顶指针
public:
    LinkStack();
    virtual ~LinkStack();
    int GetLength() const;
    bool IsEmpty() const;
    void Clear();
    Status Push(const ElemType e);
    Status Top(ElemType &e) const;
    Status Pop(ElemType &e);
    void Traverse(void (*visit)(const ElemType &)) const;
};
