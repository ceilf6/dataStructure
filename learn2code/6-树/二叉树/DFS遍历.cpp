#include "二叉链表.h"

template <class ElemType>
void BinaryTree<ElemType>::
    InOrder(BinTreeNode<ElemType> *r,
            void (*Visit)(const ElemType &)) const
{
    if (r != NULL)
    {
        InOrder(r->leftChild, Visit);
        (*Visit)(r->data);
        InOrder(r->rightChild, Visit);
    }
}

template <class ElemType>
void BinaryTree<ElemType>::
    PreOrder(BinTreeNode<ElemType> *r,
             void (*Visit)(const ElemType &)) const
{
    if (r != NULL)
    {
        (*Visit)(r->data);
        PreOrder(r->leftChild, Visit);
        PreOrder(r->rightChild, Visit);
    }
}

template <class ElemType>
void BinaryTree<ElemType>::
    PostOrder(BinTreeNode<ElemType> *r,
              void (*Visit)(const ElemType &)) const
{
    if (r != NULL)
    {
        PostOrder(r->leftChild, Visit);
        PostOrder(r->rightChild, Visit);
        (*Visit)(r->data);
    }
}
