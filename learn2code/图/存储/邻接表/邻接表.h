#ifndef ADJACENCY_LIST_H
#define ADJACENCY_LIST_H

#include <cstddef>

template <class WeightType>
struct AdjListNetworkArc;

template <class ElemType, class WeightType>
struct AdjListNetWorkVex
{
    ElemType data;
    AdjListNetworkArc<WeightType> *firstarc;

    AdjListNetWorkVex() : firstarc(NULL) {}
    AdjListNetWorkVex(ElemType val,
                      AdjListNetworkArc<WeightType> *adj = NULL)
        : data(val), firstarc(adj) {}
};

template <class WeightType>
struct AdjListNetworkArc
{
    int adjvex;
    WeightType weight;
    AdjListNetworkArc<WeightType> *next;

    AdjListNetworkArc(int v,
                      WeightType w,
                      AdjListNetworkArc *n = NULL)
        : adjvex(v), weight(w), next(n) {}
};

#endif
