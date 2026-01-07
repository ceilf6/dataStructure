#include "二叉链表.h"

template <class ElemType>
BinTreeNode<ElemType>::BinTreeNode()
{
    leftChild = rightChild = NULL;
}

template <class ElemType>
BinTreeNode<ElemType>::BinTreeNode(const ElemType &val,
                                   BinTreeNode<ElemType> *lChild = NULL,
                                   BinTreeNode<ElemType> *rChild = NULL)
{
    data = val;          // 数据元素值
    leftChild = lChild;  // 左孩子
    rightChild = rChild; // 右孩子
}
