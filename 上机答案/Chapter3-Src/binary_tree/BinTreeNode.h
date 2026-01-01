#ifndef __BIN_TREE_NODE_H__
#define __BIN_TREE_NODE_H__

// 二叉树结点类（由双向链表的DblNode改造而来）
// 将prior改名为leftChild，next改名为rightChild
template <class ElemType>
struct BinTreeNode
{
    // 数据成员:
    ElemType data;                     // 数据域
    BinTreeNode<ElemType> *leftChild;  // 指向左孩子的指针域（原prior）
    BinTreeNode<ElemType> *rightChild; // 指向右孩子的指针域（原next）

    // 构造函数:
    BinTreeNode(); // 无数据的构造函数
    BinTreeNode(ElemType item,
                BinTreeNode<ElemType> *leftlink = NULL,
                BinTreeNode<ElemType> *rightlink = NULL); // 已知数据和指针建立结构
};

// 二叉树结点类实现部分

template <class ElemType>
BinTreeNode<ElemType>::BinTreeNode()
// 操作结果：构造指针域为空的结点
{
    leftChild = NULL;
    rightChild = NULL;
}

template <class ElemType>
BinTreeNode<ElemType>::BinTreeNode(ElemType item,
                                   BinTreeNode<ElemType> *leftlink,
                                   BinTreeNode<ElemType> *rightlink)
// 操作结果：构造一个数据域为item、leftChild指针域为leftlink、rightChild指针域为rightlink的结点
{
    data = item;
    leftChild = leftlink;
    rightChild = rightlink;
}

#endif
