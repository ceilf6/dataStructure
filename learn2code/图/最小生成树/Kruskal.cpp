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
