#include "邻接表.h"

// 顶点节点无参数的构造函数
template <class ElemType, class WeightType>
AdjListNetWorkVex<ElemType, WeightType>::AdjListNetWorkVex()
{
    firstarc = NULL;
}

// 顶点节点有参数的构造函数
template <class ElemType, class WeightType>
AdjListNetWorkVex<ElemType, WeightType>::AdjListNetWorkVex(ElemType val,
                                                           AdjListNetworkArc<WeightType> *adj)
{
    data = val;
    firstarc = adj;
}

// 边、弧节点的无参数构造函数
template <class WeightType>
AdjListNetworkArc<WeightType>::AdjListNetworkArc(int v, WeightType w,
                                                 AdjListNetworkArc<WeightType> *next)
{
    adjVex = -1;
}

// 边有参数构造函数
template <class WeightType>
AdjListNetworkArc<WeightType>::AdjListNetworkArc(int v, WeightType w,
                                                 AdjListNetworkArc<WeightType> *next)
{
    adjVex = v;
    weight = w;
    nextarc = next;
}
