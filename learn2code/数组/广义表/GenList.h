enum GenListNodeType
{
    HEAD,
    ATOM,
    LIST
};
/*
  - HEAD：每个 () 的入口标记
  - ATOM：() 内的原子值
  - LIST：() 内嵌套的另一个 ()，通过 hLink 指向那个子表的 HEAD
*/
template <class ElemType>
struct GenListNode
{
    GenListNodeType tag;
    // 标志域,HEAD(0):头结点, ATOM(1):原子结构, LIST(2):表结点
    GenListNode<ElemType> *tLink;
    union
    {
        int ref;       // tag=HEAD,头结点,存放引用数
        ElemType atom; // tag=ATOM,存放原子结点的数据域
        GenListNode<ElemType> *hLink;
    };
    GenListNode(GenListNodeType tg = HEAD,
                GenListNode<ElemType> *next = NULL);
    // 由标志tag和指针next构造引用数法广义表结点
};

template <class ElemType>
class GenList
{
protected:
    GenListNode<ElemType> *head;
    void ShowHelp(GenListNode<ElemType> *hd) const;
    int DepthHelp(const GenListNode<ElemType> *hd);
    void ClearHelp(GenListNode<ElemType> *hd);
    void CopyHelp(const GenListNode<ElemType> *sourceHead,
                  GenListNode<ElemType> *&destHead);
    static void CreateHelp(GenListNode<ElemType> *&first);

public:
    GenList();
    GenList(GenListNode<ElemType> *hd);
    ~GenList();
    GenListNode<ElemType> *First() const;
    GenListNode<ElemType> *Next(GenListNode<ElemType> *p) const;
    bool IsEmpty() const;
    void Insert(const ElemType &e);
    void Insert(GenList<ElemType> &subList);
    Status Delete(int i);
    int GetDepth();
    int GetLength();
    void Input(void);
    void Show(void);
};
