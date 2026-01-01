#ifndef __BINARY_TREE_H__
#define __BINARY_TREE_H__

#include "Assistance.h"  // 辅助软件包
#include "BinTreeNode.h" // 二叉树结点类

// 二叉树类（由双向链表的DblLinkList改造而来）
// 将head改名为root
template <class ElemType>
class BinaryTree
{
protected:
    //  二叉树的数据成员:
    BinTreeNode<ElemType> *root; // 根结点指针（原head）
    int nodeCount;               // 结点个数（原length）

    // 辅助函数
    void DestroyHelp(BinTreeNode<ElemType> *r);                                          // 销毁以r为根的二叉树
    void PreOrderHelp(BinTreeNode<ElemType> *r, void (*Visit)(const ElemType &)) const;  // 前序遍历
    void InOrderHelp(BinTreeNode<ElemType> *r, void (*Visit)(const ElemType &)) const;   // 中序遍历
    void PostOrderHelp(BinTreeNode<ElemType> *r, void (*Visit)(const ElemType &)) const; // 后序遍历
    int HeightHelp(BinTreeNode<ElemType> *r) const;                                      // 返回树的高度
    int NodeCountHelp(BinTreeNode<ElemType> *r) const;                                   // 返回树的结点数
    BinTreeNode<ElemType> *CopyTreeHelp(BinTreeNode<ElemType> *r);                       // 复制树

public:
    BinaryTree();               // 无参数的构造函数
    BinaryTree(ElemType value); // 构造只有根结点的二叉树
    virtual ~BinaryTree();      // 析构函数

    BinTreeNode<ElemType> *GetRoot() const; // 返回根结点
    bool IsEmpty() const;                   // 判断二叉树是否为空
    int GetNodeCount() const;               // 返回结点个数
    int GetHeight() const;                  // 返回树的高度（深度）

    // 遍历操作
    void PreOrder(void (*Visit)(const ElemType &)) const;  // 前序遍历
    void InOrder(void (*Visit)(const ElemType &)) const;   // 中序遍历
    void PostOrder(void (*Visit)(const ElemType &)) const; // 后序遍历

    // 建树操作
    void CreateBinTree(BinTreeNode<ElemType> *&r);                      // 递归创建二叉树
    void InsertLeftChild(BinTreeNode<ElemType> *p, const ElemType &e);  // 插入左孩子
    void InsertRightChild(BinTreeNode<ElemType> *p, const ElemType &e); // 插入右孩子

    // 拷贝构造和赋值运算符
    BinaryTree(const BinaryTree<ElemType> &tree);                      // 拷贝构造函数
    BinaryTree<ElemType> &operator=(const BinaryTree<ElemType> &tree); // 重载赋值运算符
};

// 二叉树类实现部分

template <class ElemType>
BinaryTree<ElemType>::BinaryTree()
// 操作结果：构造一个空二叉树
{
    root = NULL;   // 空树根结点为NULL
    nodeCount = 0; // 初始化结点个数
}

template <class ElemType>
BinaryTree<ElemType>::BinaryTree(ElemType value)
// 操作结果：构造只有根结点的二叉树
{
    root = new BinTreeNode<ElemType>(value); // 创建根结点
    assert(root);                            // 创建根结点失败，终止程序运行
    nodeCount = 1;                           // 初始化结点个数
}

template <class ElemType>
void BinaryTree<ElemType>::DestroyHelp(BinTreeNode<ElemType> *r)
// 操作结果：销毁以r为根的二叉树
{
    if (r != NULL)
    {                               // r非空，才能销毁
        DestroyHelp(r->leftChild);  // 销毁左子树
        DestroyHelp(r->rightChild); // 销毁右子树
        delete r;                   // 销毁根结点
    }
}

template <class ElemType>
BinaryTree<ElemType>::~BinaryTree()
// 操作结果：销毁二叉树
{
    DestroyHelp(root);
}

template <class ElemType>
BinTreeNode<ElemType> *BinaryTree<ElemType>::GetRoot() const
// 操作结果：返回根结点
{
    return root;
}

template <class ElemType>
bool BinaryTree<ElemType>::IsEmpty() const
// 操作结果：如二叉树为空，则返回true，否则返回false
{
    return root == NULL;
}

template <class ElemType>
void BinaryTree<ElemType>::PreOrderHelp(BinTreeNode<ElemType> *r, void (*Visit)(const ElemType &)) const
// 操作结果：前序遍历以r为根的二叉树（递归算法）
{
    if (r != NULL)
    {
        (*Visit)(r->data);                  // 访问根结点
        PreOrderHelp(r->leftChild, Visit);  // 前序遍历左子树
        PreOrderHelp(r->rightChild, Visit); // 前序遍历右子树
    }
}

template <class ElemType>
void BinaryTree<ElemType>::PreOrder(void (*Visit)(const ElemType &)) const
// 操作结果：前序遍历二叉树
{
    PreOrderHelp(root, Visit);
}

template <class ElemType>
void BinaryTree<ElemType>::InOrderHelp(BinTreeNode<ElemType> *r, void (*Visit)(const ElemType &)) const
// 操作结果：中序遍历以r为根的二叉树（递归算法）
{
    if (r != NULL)
    {
        InOrderHelp(r->leftChild, Visit);  // 中序遍历左子树
        (*Visit)(r->data);                 // 访问根结点
        InOrderHelp(r->rightChild, Visit); // 中序遍历右子树
    }
}

template <class ElemType>
void BinaryTree<ElemType>::InOrder(void (*Visit)(const ElemType &)) const
// 操作结果：中序遍历二叉树
{
    InOrderHelp(root, Visit);
}

template <class ElemType>
void BinaryTree<ElemType>::PostOrderHelp(BinTreeNode<ElemType> *r, void (*Visit)(const ElemType &)) const
// 操作结果：后序遍历以r为根的二叉树（递归算法）
{
    if (r != NULL)
    {
        PostOrderHelp(r->leftChild, Visit);  // 后序遍历左子树
        PostOrderHelp(r->rightChild, Visit); // 后序遍历右子树
        (*Visit)(r->data);                   // 访问根结点
    }
}

template <class ElemType>
void BinaryTree<ElemType>::PostOrder(void (*Visit)(const ElemType &)) const
// 操作结果：后序遍历二叉树
{
    PostOrderHelp(root, Visit);
}

template <class ElemType>
int BinaryTree<ElemType>::HeightHelp(BinTreeNode<ElemType> *r) const
// 操作结果：返回以r为根的二叉树的高度（递归算法）
{
    if (r == NULL)
        return 0; // 空树高度为0
    else
    {
        int leftHeight = HeightHelp(r->leftChild);                        // 左子树高度
        int rightHeight = HeightHelp(r->rightChild);                      // 右子树高度
        return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight); // 树高为左右子树最大高度+1
    }
}

template <class ElemType>
int BinaryTree<ElemType>::GetHeight() const
// 操作结果：返回二叉树的高度（深度）
{
    return HeightHelp(root);
}

template <class ElemType>
int BinaryTree<ElemType>::NodeCountHelp(BinTreeNode<ElemType> *r) const
// 操作结果：返回以r为根的二叉树的结点数（递归算法）
{
    if (r == NULL)
        return 0; // 空树结点数为0
    else
        return 1 + NodeCountHelp(r->leftChild) + NodeCountHelp(r->rightChild); // 结点数为左右子树结点数之和+1
}

template <class ElemType>
int BinaryTree<ElemType>::GetNodeCount() const
// 操作结果：返回二叉树的结点个数
{
    return NodeCountHelp(root);
}

template <class ElemType>
void BinaryTree<ElemType>::InsertLeftChild(BinTreeNode<ElemType> *p, const ElemType &e)
// 操作结果：给结点p插入左孩子，数据为e
{
    if (p != NULL)
    {
        BinTreeNode<ElemType> *child = new BinTreeNode<ElemType>(e);
        assert(child);
        p->leftChild = child;
        nodeCount++;
    }
}

template <class ElemType>
void BinaryTree<ElemType>::InsertRightChild(BinTreeNode<ElemType> *p, const ElemType &e)
// 操作结果：给结点p插入右孩子，数据为e
{
    if (p != NULL)
    {
        BinTreeNode<ElemType> *child = new BinTreeNode<ElemType>(e);
        assert(child);
        p->rightChild = child;
        nodeCount++;
    }
}

template <class ElemType>
BinTreeNode<ElemType> *BinaryTree<ElemType>::CopyTreeHelp(BinTreeNode<ElemType> *r)
// 操作结果：复制以r为根的二叉树，返回新树的根结点指针
{
    if (r == NULL)
        return NULL;
    else
    {
        BinTreeNode<ElemType> *newNode = new BinTreeNode<ElemType>(r->data);
        assert(newNode);
        newNode->leftChild = CopyTreeHelp(r->leftChild);   // 复制左子树
        newNode->rightChild = CopyTreeHelp(r->rightChild); // 复制右子树
        return newNode;
    }
}

template <class ElemType>
BinaryTree<ElemType>::BinaryTree(const BinaryTree<ElemType> &tree)
// 操作结果：拷贝构造，从已知二叉树tree构造新二叉树
{
    root = CopyTreeHelp(tree.root); // 复制树
    nodeCount = tree.nodeCount;     // 复制结点数
}

template <class ElemType>
BinaryTree<ElemType> &BinaryTree<ElemType>::operator=(const BinaryTree<ElemType> &tree)
// 操作结果：赋值运算符重载，将二叉树tree赋值给当前二叉树
{
    if (&tree != this)
    {
        DestroyHelp(root);              // 销毁原树
        root = CopyTreeHelp(tree.root); // 复制树
        nodeCount = tree.nodeCount;     // 复制结点数
    }
    return *this;
}

#endif
