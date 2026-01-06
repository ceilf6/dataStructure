#ifndef SHARE_STACK_H
#define SHARE_STACK_H

#include <iostream>

#define MAXSIZE 100

typedef int ElemType;

class ShareStack
{
private:
    ElemType data[MAXSIZE];
    int top1;
    int top2;

public:
    ShareStack();

    bool isEmpty(int stackNum) const;
    bool isFull() const;

    bool push(int stackNum, ElemType x);
    bool pop(int stackNum, ElemType &x);

    void print() const;
};

#endif // SHARE_STACK_H