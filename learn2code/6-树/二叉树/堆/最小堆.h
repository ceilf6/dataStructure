#include "Status.h"

template <class ElemType>
class MinHeap
{
private:
    ElemType *heapArr;
    int CurrentSize;
    int MaxSize;
    void FilterDown(int Start);
    void FilterUp(int End);

public:
    MinHeap(int maxSize);
    MinHeap(ElemType a[], int maxsize, int n);
    ~MinHeap() { delete[] heapArr; }
    Status Insert(const ElemType &e);
    Status DeleteTop(ElemType &e);
    Status GetTop(ElemType &e) const;
    bool IsEmpty() const { return CurrentSize == 0; }
    bool IsFull() const { return CurrentSize == MaxSize; }
    int SizeOfHeap() const { return CurrentSize; }
    void SetEmpty() { CurrentSize = 0; }
    void Traverse(void (*Visit)(const ElemType &)) const;
};
