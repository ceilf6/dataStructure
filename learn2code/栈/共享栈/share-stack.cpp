#include "share-stack.h"

ShareStack::ShareStack()
{
    top1 = -1;
    top2 = MAXSIZE;
}

bool ShareStack::isEmpty(ShareStack::stackNum sn) const
{
    if (sn == ShareStack::stack1)
        return top1 == -1;
    else if (sn == ShareStack::stack2)
        return top2 == MAXSIZE;
    return true;
}

bool ShareStack::isFull() const
{
    return top1 + 1 == top2;
}

bool ShareStack::push(ShareStack::stackNum sn, ElemType x)
{
    if (isFull())
        return false;

    if (sn == ShareStack::stack1)
    {
        data[++top1] = x;
        return true;
    }
    else if (sn == ShareStack::stack2)
    {
        data[--top2] = x;
        return true;
    }
    return false;
}

bool ShareStack::pop(ShareStack::stackNum sn, ElemType &x)
{
    if (sn == ShareStack::stack1)
    {
        if (isEmpty(ShareStack::stack1))
            return false;
        x = data[top1--];
        return true;
    }
    else if (sn == ShareStack::stack2)
    {
        if (isEmpty(ShareStack::stack2))
            return false;
        x = data[top2++];
        return true;
    }
    return false;
}

void ShareStack::print() const
{
    std::cout << "Stack1: ";
    for (int i = 0; i <= top1; ++i)
        std::cout << data[i] << " ";
    std::cout << std::endl;

    std::cout << "Stack2: ";
    for (int i = MAXSIZE - 1; i >= top2; --i)
        std::cout << data[i] << " ";
    std::cout << std::endl;
}