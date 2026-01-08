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
