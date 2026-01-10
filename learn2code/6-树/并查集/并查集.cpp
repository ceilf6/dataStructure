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
// 加权规则 - 考试只要求 1 （后面两个贴在最后）
// 1. 按规模合并
template <class ElemType>
void UFSets<ElemType>::
    Union(ElemType a, ElemType b)
{
    int r1 = Find(a);
    int r2 = Find(b);
    if (r1 != r2 && r1 != -1)
    {
        int temp = sets[r1].parent + sets[r2].parent;
        if (sets[r1].parent <= sets[r2].parent)
        {
            sets[r2].parent = r1;
            sets[r1].parent = temp;
        }
        else
        {
            sets[r1].parent = r2;
            sets[r2].parent = temp;
        }
    }
}

// Differ 判断是否属于不同集合：直接判断根是否相同
template <class ElemType>
bool UFSets<ElemType>::Differ(ElemType a, ElemType b)
{
    return Find(a) != Find(b);
}

// 折叠规则压缩路径的查找算法
template <class ElemType>
int UFSets<ElemType>::Find(ElemType e) // PPT 中加了 const ，但是后面会修改 sets[p].parent 做路径压缩。接口写 const 在 C++ 里是不合理的：除非 sets 被声明成 mutable，否则编译器会报错或你贴的不是最终版本。
{
    int i, k, p = 0;
    while (p < size && sets[p].data != e)
        p++;
    if (p == size)
        return -1;
    for (i = p; sets[i].parent >= 0; i = sets[i].parent)
        ;
    while (i != sets[p].parent) // 把从原始结点 p 到根 i 的整条路径上的结点，parent 全部改成 i。
    {
        k = sets[p].parent;
        sets[p].parent = i; // 让 p 直接指向根 i。
        p = k;
    }
    return i;
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