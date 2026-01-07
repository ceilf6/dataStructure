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

// 查：查找元素所在集合的根（没路径压缩
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

// 并：让一个根指向另一个根（没有按秩合并
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
// 加权规则
// 1. 按规模合并
template <class ElemType>
void UFSets<ElemType>::Union(ElemType a, ElemType b)
{
    int ra = Find(a);
    int rb = Find(b);

    if (ra == -1 || rb == -1 || ra == rb)
        return;

    // ra、rb 都是根，parent 为负数，绝对值表示规模
    if (sets[ra].parent < sets[rb].parent)
    {
        // ra 的规模更大
        sets[ra].parent += sets[rb].parent;
        sets[rb].parent = ra;
    }
    else
    {
        sets[rb].parent += sets[ra].parent;
        sets[ra].parent = rb;
    }
}
// 2. 按高度合并
template <class ElemType>
void UFSets<ElemType>::Union(ElemType a, ElemType b)
{
    int ra = Find(a);
    int rb = Find(b);

    if (ra == -1 || rb == -1 || ra == rb)
        return;

    // 高度比较（parent 的绝对值）
    if (sets[ra].parent < sets[rb].parent)
    {
        // ra 更高
        sets[rb].parent = ra;
    }
    else if (sets[ra].parent > sets[rb].parent)
    {
        // rb 更高
        sets[ra].parent = rb;
    }
    else
    {
        // 高度相同，合并后高度 +1
        sets[rb].parent = ra;
        sets[ra].parent--;
    }
}
// 3. 按秩合并
template <class ElemType>
void UFSets<ElemType>::Union(ElemType a, ElemType b)
{
    int ra = Find(a);
    int rb = Find(b);

    if (ra == -1 || rb == -1 || ra == rb)
        return;

    // rank 存在 parent 的绝对值中
    if (sets[ra].parent < sets[rb].parent)
    {
        // ra 的 rank 更大
        sets[rb].parent = ra;
    }
    else if (sets[ra].parent > sets[rb].parent)
    {
        sets[ra].parent = rb;
    }
    else
    {
        // rank 相等
        sets[rb].parent = ra;
        sets[ra].parent--; // rank +1
    }
}

// Differ 判断是否属于不同集合：直接判断根是否相同
template <class ElemType>
bool UFSets<ElemType>::Differ(ElemType a, ElemType b)
{
    return Find(a) != Find(b);
}