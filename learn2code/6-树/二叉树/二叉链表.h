template <class ElemType>
struct BinTreeNode
{
    ElemType data;                     // 数据域
    BinTreeNode<ElemType> *leftChild;  // 左孩子指针域
    BinTreeNode<ElemType> *rightChild; // 右孩子指针域
    BinTreeNode();                     // 无参数的构造函数
    BinTreeNode(const ElemType &val,
                BinTreeNode<ElemType> *lChild = NULL,
                BinTreeNode<ElemType> *rChild = NULL);
};

template <class ElemType>
class BinaryTree
{
protected:
    BinTreeNode<ElemType> *root;
    BinTreeNode<ElemType> *CopyTree(BinTreeNode<ElemType> *t);
    void Destroy(BinTreeNode<ElemType> *&r);
    void PreOrder(BinTreeNode<ElemType> *r,
                  void (*Visit)(const ElemType &)) const;
    void InOrder(BinTreeNode<ElemType> *r,
                 void (*Visit)(const ElemType &)) const;
    void PostOrder(BinTreeNode<ElemType> *r,
                   void (*Visit)(const ElemType &)) const;
    int Height(const BinTreeNode<ElemType> *r) const;
    int NodeCount(const BinTreeNode<ElemType> *r) const;
    BinTreeNode<ElemType> *Parent(BinTreeNode<ElemType> *r,
                                  const BinTreeNode<ElemType> *p) const;

public:
    BinaryTree();
    virtual ~BinaryTree();
    BinTreeNode<ElemType> *GetRoot() const;
    bool IsEmpty() const;
    Status GetElem(BinTreeNode<ElemType> *p, ElemType &e) const;
    Status SetElem(BinTreeNode<ElemType> *p, const ElemType &e);
    void InOrder(void (*Visit)(const ElemType &)) const;
    void PreOrder(void (*Visit)(const ElemType &)) const;
    void PostOrder(void (*Visit)(const ElemType &)) const;
    void LevelOrder(void (*Visit)(const ElemType &)) const;
    int NodeCount() const;
    BinTreeNode<ElemType> *LeftChild(const BinTreeNode<ElemType> *p) const;
    BinTreeNode<ElemType> *RightChild(const BinTreeNode<ElemType> *p) const;
    void InsertLeftChild(BinTreeNode<ElemType> *p, const ElemType &e);
    void InsertRightChild(BinTreeNode<ElemType> *p, const ElemType &e);
    void DeleteLeftChild(BinTreeNode<ElemType> *p);
    void DeleteRightChild(BinTreeNode<ElemType> *p);
    int Height() const;
    BinaryTree(const BinaryTree<ElemType> &t);
    BinaryTree(BinTreeNode<ElemType> *r);
    BinaryTree<ElemType> &operator=(const BinaryTree<ElemType> &t);
    BinTreeNode<ElemType> *LeftSibling(const BinTreeNode<ElemType> *p) const;
};
