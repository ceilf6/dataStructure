#include "share-stack.h"

int main()
{
    ShareStack s;
    int x;

    s.push(ShareStack::stack1, 10);
    s.push(ShareStack::stack1, 20);
    s.push(ShareStack::stack2, 100);
    s.push(ShareStack::stack2, 200);

    s.print();

    s.pop(ShareStack::stack1, x);
    s.pop(ShareStack::stack2, x);

    s.print();
    return 0;
}