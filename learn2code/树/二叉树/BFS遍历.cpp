#include "二叉链表.h"
#include "queue.h"

template <class ElemType>
void BinaryTree<ElemType>::LevelOrder(void (*Visit)(const ElemType &)) const
{
    LinkQueue<BinTreeNode<ElemType> *> q;
    BinTreeNode<ElemType> *p;
    if (root != NULL)
        q.EnQueue(root);
    while (!q.IsEmpty())
    {
        q.DelQueue(p);
        (*Visit)(p->data);
        if (p->leftChild != NULL)
            q.EnQueue(p->leftChild);
        if (p->rightChild != NULL)
            q.EnQueue(p->rightChild);
    }
}
