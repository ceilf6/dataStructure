template <class ElemType, class WeightType>
struct AdjListNetWorkVex
{
    ElemType data;
    AdjListNetworkArc<WeightType> *firstarc;

    AdjListNetWorkVex();
    AdjListNetWorkVex(ElemType val,
                      AdjListNetworkArc<WeightType> *adj = NULL);
};
