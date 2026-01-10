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
    enum stackNum
    {
        stack1 = 1,
        stack2 = 2
    };

    ShareStack();

    bool isEmpty(stackNum sn) const;
    bool isFull() const;

    bool push(stackNum sn, ElemType x);
    bool pop(stackNum sn, ElemType &x);

    void print() const;
};

#endif // SHARE_STACK_H