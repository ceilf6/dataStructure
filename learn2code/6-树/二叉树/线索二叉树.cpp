#include "线索二叉树.h"

// 通过Help封装递归过程
template <class ElemType>
void InThreadBinTree<ElemType>::
    InThreadHelp(ThreadBinTreeNode<ElemType> *p,
                 ThreadBinTreeNode<ElemType> *&pre)
{
    if (p != NULL)
    {
        InThreadHelp(p->leftChild, pre);
        if (p->leftChild == NULL)
        {
            p->leftChild = pre; // 携带下来的前驱信息
            p->leftTag = 1;
        }
        else
            p->leftTag = 0;
        if (pre != NULL && pre->rightChild == NULL)
        {
            pre->rightChild = p; // pre的后继节点应该是p（PPT中的r错了）
            pre->rightTag = 1;
        }
        else if (pre != NULL)
            pre->rightTag = 0;
        pre = p; // 更新前驱信息
        InThreadHelp(p->rightChild, pre);
    }
}

// 向外暴露的只有调用接口
template <class ElemType>
void InThreadBinTree<ElemType>::InThread()
{
    ThreadBinTreeNode<ElemType> *pre = NULL;
    InThreadHelp(root, pre);
    pre->rightTag = 1;
}

// 找中序序列第一个节点：即最左边的那个节点
template <class ElemType>
ThreadBinTreeNode<ElemType> *InThreadBinTree<ElemType>::GetFirst() const
{
    if (root == NULL)
        return NULL;
    else
    {
        ThreadBinTreeNode<ElemType> *p = root;
        while (p->leftTag == 0)
            p = p->leftChild;
        return p;
    }
}

// 找中序线索二叉树的中序遍历下一个元素
template <class ElemType>
ThreadBinTreeNode<ElemType> *InThreadBinTree<ElemType>::GetNext(ThreadBinTreeNode<ElemType> *p) const
{
    if (p->rightTag == 1)
        p = p->rightChild;
    else
    {
        p = p->rightChild;
        /*
        // 进入右子树中来一遍左根右，所以紧接就是右子树的最左边
        // 而中序线索化之后 leftChild 就能帮助快速向左
        */
        while (p->leftTag == 0)
            p = p->leftChild;
    }
    return p;
}

template <class ElemType>
void InThreadBinTree<ElemType>::InOrder(void (*Visit)(const ElemType &)) const
{
    ThreadBinTreeNode<ElemType> *p;
    for (p = GetFirst(); p != NULL; p = GetNext(p))
    {
        (*Visit)(p->data);
        if (p->leftTag == 1)
            cout << "其左指针为线索指针，指向";
        else
            cout << "其左指针为孩子指针，指向";
        if (p->leftChild != NULL)
            cout << p->leftChild->data;
        else
            cout << "NULL";
        if (p->rightTag == 1)
            cout << "；其右指针为线索指针，指向";
        else
            cout << "；其右指针为孩子指针，指向";
        if (p->rightChild != NULL)
            cout << p->rightChild->data << endl;
        else
            cout << "NULL" << endl;
    }
}

template <class ElemType>
void InThreadBinTree<ElemType>::
    InsertRightChild(ThreadBinTreeNode<ElemType> *p, const ElemType &e)
{
    ThreadBinTreeNode<ElemType> *x, *q;
    if (p == NULL)
        return;
    else
    {
        /*
        插在 p 的右边中序前驱一定是 p
        新节点的右边就是直接继承 p 的右边
        1. 这样就实现了新节点左右两边的连贯
        */
        x = new ThreadBinTreeNode<ElemType>(e, p,
                                            p->rightChild, 1, p->rightTag); // 生成元素值为e结点x
        if (p->rightTag == 0)
        /*
        2. 实现新节点右边到新节点的连贯
        右子树的最左节点的前驱必须改为新节点
        */
        {
            q = p->rightChild;
            while (q->leftTag == 0)
                q = q->leftChild;
            q->leftChild = x;
        }
        /*
        3. 最后实现新节点左边也就是插入目标元素 p 到新节点的连贯
        */
        p->rightChild = x;
        p->rightTag = 0;
        return;
    }
}

template <class ElemType>
void InThreadBinTree<ElemType>::
    DeleteLeftChild(ThreadBinTreeNode<ElemType> *p)
{
    ThreadBinTreeNode<ElemType> *x, *q;
    if (p == NULL || p->leftTag != 0)
        return;
    else
    {
        q = p->leftChild;
        while (q->leftTag == 0) // 删除当前节点的右子树
            q = q->leftChild;
        q = q->leftChild;
        DestroyHelp(p->leftChild); // 复用：删除当前节点的左子树
        p->leftChild = q;
        p->leftTag = 1;
        return;
    }
}
