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

template <class ElemType>
void BinaryTree<ElemType>::
    Destroy(BinTreeNode<ElemType> *&r)
{
    if (r != NULL) // 递归删除左右子树
    {
        Destroy(r->leftChild);
        Destroy(r->rightChild);
        delete r;
        r = NULL;
    }
}

// 找父节点
template <class ElemType>
BinTreeNode<ElemType> *BinaryTree<ElemType>::Parent(BinTreeNode<ElemType> *r,
                                                    const BinTreeNode<ElemType> *p) const
{
    if (r == NULL) // 边界：叶子下面或者空树
        return NULL;
    else if (r->leftChild == p || r->rightChild == p) // 如果孩子有目标那么这就是父节点
        return r;
    else
    {
        BinTreeNode<ElemType> *tmp;
        // 如果递归传上来的不是空，那么就说明有目标，直接上传就好
        tmp = Parent(r->leftChild, p);
        if (tmp != NULL)
            return tmp;
        tmp = Parent(r->rightChild, p);
        if (tmp != NULL)
            return tmp;
        else
            return NULL;
    }
}

// 左兄弟
template <class ElemType>
BinTreeNode<ElemType> *BinaryTree<ElemType>::LeftSibling(const BinTreeNode<ElemType> *p) const
{
    BinTreeNode<ElemType> *r = Parent(root, p);
    if (r == NULL)
        return NULL;
    else if (r->rightChild == p)
        return r->leftChild;
    else
        return NULL;
}

// 插入右孩子
template <class ElemType>
void BinaryTree<ElemType>::
    InsertRightChild(BinTreeNode<ElemType> *p, const ElemType &e)
{
    if (p == NULL)
        return;
    else
    {
        BinTreeNode<ElemType> *child = new BinTreeNode<ElemType>(e);
        if (p->rightChild != NULL)
            child->rightChild = p->rightChild; // 将原先的右孩子作为新节点的右子树
        p->rightChild = child;
        return;
    }
}
