template <class ElemType>
struct DblNode
{
    ElemType data;
    DblNode<ElemType> *prior;
    DblNode<ElemType> *next;

    DblNode();
    DblNode(ElemType e,
            DblNode<ElemType> *priorlink = NULL,
            DblNode<ElemType> *nextlink = NULL);
};
template <class ElemType>
DblNode<ElemType>::DblNode()
{
    prior = NULL;
    next = NULL;
}
template <class ElemType>
DblNode<ElemType>::DblNode(ElemType e,
                           DblNode<ElemType> *priorlink,
                           DblNode<ElemType> *nextlink)
{
    data = e;
    prior = priorlink;
    next = nextlink;
}

template <class ElemType>
class DblLinkList
{
protected:
    DblNode<ElemType> *head;
    int length;

public:
    enum Status
    {
        SUCCESS,
        FAILED
        // ...
    };

    DblLinkList();
    DblLinkList(ElemType v[], int n);
    virtual ~DblLinkList();
    int GetLength() const;
    bool IsEmpty() const;
    void Clear();
    void Traverse(void (*Visit)(const ElemType &)) const;
    int LocateElem(const ElemType &e);
    Status GetElem(int i, ElemType &e) const;
    Status GetElem(int i, ElemType &e) const;
    Status SetElem(int i, const ElemType &e);
    Status DeleteElem(int i, ElemType &e);
    Status InsertElem(int i, const ElemType &e);
    Status InsertElem(const ElemType &e);
    DblLinkList(const DblLinkList<ElemType> &la);
    DblLinkList<ElemType> &operator=(const DblLinkList<ElemType> &la);
};
