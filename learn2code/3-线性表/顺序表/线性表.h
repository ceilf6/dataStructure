template <typename ElemType> // template 是一个类型占位符 , 使用时通过 SeqList<int> 确定类型

class SeqList
{
protected:
    int length; // 当前表有效长
    int maxLength;
    ElemType *elems; // elems 是一个指向 ElemType 类型的数组指针

public:
    enum Status
    {
        NOT_PRESENT,
        ENTRY_FOUND
        // ...
    };

    SeqList(int size = DEFAULT_SIZE);
    SeqList(ElemType v[], int n, int size = DEFAULT_SIZE);
    virtual ~SeqList();
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
    SeqList(const SeqList<ElemType> &sa);
    SeqList<ElemType> &operator=(const SeqList<ElemType>
                                     &sa);
};
