#include "并查集.h"

template <class ElemType>
UFSets<ElemType>::UFSets(ElemType es[], int n)
{
    size = n;
    sets = new ElemNode<ElemType>[size];
    for (int i = 0; i < size; i++)
    {
        sets[i].data = es[i];
        sets[i].parent = -1;
    }
}

template <class ElemType>
int UFSets<ElemType>::GetOrder(ElemType e) const
{
    int p = 0;
    while (p < size && sets[p].data != e)
        p++;
    if (p == size)
        return -1;
    return p;
}

template <class ElemType>
int UFSets<ElemType>::Find(ElemType e) const
{
    int p = 0;
    while (p < size && sets[p].data != e)
        p++;
    if (p == size)
        return -1;
    while (sets[p].parent > -1)
        p = sets[p].parent;
    return p;
}

template <class ElemType>
void UFSets<ElemType>::Union(ElemType a, ElemType b)
{
    int r1 = Find(a);
    int r2 = Find(b);
    if (r1 != r2 && r1 != -1)
    {
        sets[r1].parent += sets[r2].parent;
        sets[r2].parent = r1;
    }
}
