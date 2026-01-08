#ifndef ADJACENCY_LIST_H
#define ADJACENCY_LIST_H

#include <cstddef>

template <class WeightType>
struct AdjListNetworkArc;

// 每个邻接表链表的头节点
template <class ElemType, class WeightType>
struct AdjListNetWorkVex
{
    ElemType data;                           // 顶点信息
    AdjListNetworkArc<WeightType> *firstarc; // 第一条边（头节点）

    AdjListNetWorkVex() : firstarc(NULL) {}
    AdjListNetWorkVex(ElemType val,
                      AdjListNetworkArc<WeightType> *adj = NULL)
        : data(val), firstarc(adj) {}
};

// 邻接表中每一条边的节点结构
template <class WeightType>
struct AdjListNetworkArc
{
    int adjvex;                             // 顶点数组中的下标，标识这条边是连向哪个顶点
    WeightType weight;                      // 边权值
    AdjListNetworkArc<WeightType> *nextarc; // 指向同一顶点的下一条边

    AdjListNetworkArc(int v,
                      WeightType w,
                      AdjListNetworkArc *n = NULL)
        : adjvex(v), weight(w), nextarc(n) {}
};

/*
AdjListNetWorkVex vertexes[vexNum];

vertexes[0] --> arc0_1 -> arc0_2 -> arc0_3 -> NULL
vertexes[1] --> arc1_1 -> arc1_2 -> NULL
vertexes[2] --> NULL
...
*/

#endif
