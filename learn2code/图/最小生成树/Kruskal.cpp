#include "Kruskal.h"

template <class ElemType, class WeightType>
KruskalEdge<ElemType, WeightType>::
    KruskalEdge(ElemType v1, ElemType v2, WeightType w)
{
    vertex1 = v1; // 顶点vertex1
    vertex2 = v2; // 顶点vertex2
    weight = w;   // 权weight
}

// 比较符重载实现Cmp
template <class ElemType, class WeightType>
bool KruskalEdge<ElemType, WeightType>::operator<=(const KruskalEdge<ElemType, WeightType> &Ed)
{
    return (weight <= Ed.weight);
}

template <class ElemType, class WeightType>
KruskalEdge<ElemType, WeightType> &KruskalEdge<ElemType, WeightType>::operator=(const KruskalEdge<ElemType, WeightType> &Ed)
{
    if (&Ed != this)
    {
        vertex1 = Ed.vertex1;
        vertex2 = Ed.vertex2;
        weight = Ed.weight;
    }
    return *this;
}

template <class ElemType, class WeightType>
bool KruskalEdge<ElemType, WeightType>::
operator<=(const KruskalEdge<ElemType, WeightType> &Ed)
{
    return (weight > Ed.weight);
}

template <class ElemType, class WeightType>
void MiniSpanTreeKruskal(const AdjMatrixUndirNetwork<ElemType, WeightType> &g)
{
    int count, VexNum = g.GetVexNum();
    KruskalEdge<ElemType, WeightType> KEdge;
    MinHeap<KruskalEdge<ElemType, WeightType>>
        ha(g.GetEdgeNum());
    ElemType *kVex, v1, v2;
    kVex = new ElemType[VexNum];
    for (int i = 0; i < VexNum; i++)
        g.GetElem(i, kVex[i]);
    UFSets<ElemType> f(kVex, VexNum);
    for (int v = 0; v < g.GetVexNum(); v++) // 将所有边插入堆
        for (int u = g.FirstAdjVex(v); u >= 0; u = g.NextAdjVex(v, u))
            if (v < u)
            {
                g.GetElem(v, v1);
                g.GetElem(u, v2);
                KEdge.vertex1 = v1;
                KEdge.vertex2 = v2;
                KEdge.weight = g.GetWeight(v, u);
                ha.Insert(KEdge);
            }
    count = 0;
    while (count < VexNum - 1)
    {
        ha.DeleteTop(KEdge);
        v1 = KEdge.vertex1;
        v2 = KEdge.vertex2;
        if (f.Differ(v1, v2))
        {
            cout << "边:( " << v1 << ", " << v2
                 << " ) 权:" << KEdge.weight << endl;
            f.Union(v1, v2);
            count++;
        }
    }
}
