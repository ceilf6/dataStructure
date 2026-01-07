template <class ElemType>
struct ElemNode
{
    ElemType data;
    int parent;
};

template <class Type>
class UFSets;
template <class ElemType>
class UFSets
{
protected:
    ElemNode<ElemType> *sets;
    int size;
    int Find(ElemType e) const;

public:
    UFSets(ElemType es[], int n);
    virtual ~UFSets();
    ElemType GetElem(int p) const;
    int GetOrder(ElemType e) const;
    void Union(ElemType a, ElemType b);
    bool Differ(ElemType a, ElemType b);
    UFSets(const UFSets &t);
    UFSets &operator=(const UFSets &t);
};
