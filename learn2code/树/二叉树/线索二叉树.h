/*
n个节点的二叉树有 2n 个指针，由于分支只有 n-1 条，所以 n+1 个指针是空虚的
那么可以通过线索化利用
如果
- 左指针空虚，那么指向前驱
- 右指针空虚，那么指向后继

如果设的是中序遍历的前面一个和后面一个，那么就是中序线索化
前序和后序线索化同理

不设虚拟头节点的情况下，最后只剩下 (n+1)-(n-1) = 2个空指针域
*/

template <class ElemType>
struct ThreadBinTreeNode
{
    ElemType data;
    ThreadBinTreeNode<ElemType> *leftChild;
    ThreadBinTreeNode<ElemType> *rightChild;
    int leftTag, rightTag; // 原先是否为空，现在是否为向前驱或后继的指针
    ThreadBinTreeNode();
    ThreadBinTreeNode(const ElemType &d,
                      ThreadBinTreeNode<ElemType> *lChild = NULL,
                      ThreadBinTreeNode<ElemType> *rChild = NULL,
                      int leftTag = 0, int rightTag = 0);
};

template <class ElemType>
class InThreadBinTree
{
protected:
    ThreadBinTreeNode<ElemType> *root;
    void InThreadHelp(ThreadBinTreeNode<ElemType> *p,
                      ThreadBinTreeNode<ElemType> *&pre);
    ThreadBinTreeNode<ElemType> *TransformHelp(
        BinTreeNode<ElemType> *r);
    ThreadBinTreeNode<ElemType> *CopyTreeHelp(
        ThreadBinTreeNode<ElemType> *t);
    void DestroyHelp(ThreadBinTreeNode<ElemType> *&r);

public:
    InThreadBinTree(const BinaryTree<ElemType> &bt);
    virtual ~InThreadBinTree();
    ThreadBinTreeNode<ElemType> *GetRoot() const;
    void InThread();
    ThreadBinTreeNode<ElemType> *GetFirst() const;
    ThreadBinTreeNode<ElemType> *GetLast() const;
    ThreadBinTreeNode<ElemType> *GetNext(ThreadBinTreeNode<ElemType> *p) const;
    void InsertRightChild(ThreadBinTreeNode<ElemType> *p,
                          const ElemType &e);
    void DeleteLeftChild(ThreadBinTreeNode<ElemType> *p);
    void InOrder(void (*Visit)(const ElemType &)) const;
    InThreadBinTree(const InThreadBinTree<ElemType> &t);
    InThreadBinTree<ElemType> &operator=(
        const InThreadBinTree<ElemType> &t);
};
