#include "share-stack.h"

ShareStack::ShareStack()
{
    top1 = -1;
    top2 = MAXSIZE;
}

bool ShareStack::isEmpty(int stackNum) const
{
    if (stackNum == 1)
        return top1 == -1;
    else if (stackNum == 2)
        return top2 == MAXSIZE;
    return true;
}

bool ShareStack::isFull() const
{
    return top1 + 1 == top2;
}

bool ShareStack::push(int stackNum, ElemType x)
{
    if (isFull())
        return false;

    if (stackNum == 1)
    {
        data[++top1] = x;
        return true;
    }
    else if (stackNum == 2)
    {
        data[--top2] = x;
        return true;
    }
    return false;
}

bool ShareStack::pop(int stackNum, ElemType &x)
{
    if (stackNum == 1)
    {
        if (isEmpty(1))
            return false;
        x = data[top1--];
        return true;
    }
    else if (stackNum == 2)
    {
        if (isEmpty(2))
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