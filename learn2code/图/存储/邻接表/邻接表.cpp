#include "邻接表.h"
template <class ElemType, class WeightType>
struct AdjListNetWorkVex
{
    ElemType data;
    AdjListNetworkArc<WeightType> *firstarc;

    AdjListNetWorkVex();
    AdjListNetWorkVex(ElemType val,
                      AdjListNetworkArc<WeightType> *adj = NULL);
};

template <class ElemType, class WeightType>
AdjListNetWorkVex<ElemType, WeightType>::AdjListNetWorkVex()
{
    firstarc = NULL;
}
