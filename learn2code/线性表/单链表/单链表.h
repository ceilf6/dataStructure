template <class ElemType>
struct Node // 节点类
{
    ElemType data;
    Node<ElemType> *next;

    Node();
    Node(ElemType e, Node<ElemType> *link = NULL);
};
// 节点的构造函数
template <class ElemType>
Node<ElemType>::Node()
{
    next = NULL;
}
template <class ElemType>
Node<ElemType>::Node(ElemType e, Node<ElemType> *link)
{
    data = e;
    next = link;
}

template <class ElemType>
class LinkList
{
protected:
    Node<ElemType> *head;
    int length;

public:
    enum Status
    {
        SUCCESS,
        FAILED,
        RANGE_ERROR,
        ENTRY_FOUND
        // ...
    }; // 别忘记分号

    LinkList();
    LinkList(ElemType v[], int n);
    virtual ~LinkList();
    int GetLength() const;
    bool IsEmpty() const;
    void Clear();
    void Traverse(void (*Visit)(const ElemType &)) const;
    int LocateElem(const ElemType &e) const;
    Status GetElem(int i, ElemType &e) const;
    Status SetElem(int i, const ElemType &e);
    Status DeleteElem(int i, ElemType &e);
    Status InsertElem(int i, const ElemType &e);
    Status InsertElem(const ElemType &e);
    LinkList(const LinkList<ElemType> &la);
    LinkList<ElemType> &operator=(const LinkList<ElemType> &la);
    void reverse(Node<ElemType> *p) const;
};
