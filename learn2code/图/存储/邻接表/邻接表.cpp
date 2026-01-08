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

// 有向图邻接表构造函数
template <class ElemType, class WeightType>
AdjListDirNetwork<ElemType, WeightType>::AdjListDirNetwork(int vertexMaxNum,
                                                           WeightType infinit)
{
    if (vertexMaxNum < 0)
        throw Error("允许的顶点最大数目不能为负!");
    vexNum = 0;
    vexMaxNum = vertexMaxNum;
    arcNum = 0;
    infinity = infinit;
    tag = new Status[vexMaxNum];
    vexTable = new AdjListNetWorkVex<ElemType,
                                     WeightType>[vexMaxNum];
}

// 带顶点信息的构造函数
template <class ElemType, class WeightType>
AdjListDirNetwork<ElemType, WeightType>::AdjListDirNetwork(ElemType es[],
                                                           int vertexNum, int vertexMaxNum, WeightType infinit)
{
    if (vertexMaxNum < 0)
        throw Error("允许的顶点最大数目不能为负!");
    if (vertexMaxNum < vertexNum)
        throw Error("顶点数目不能大于允许的顶点最大数目!");
    vexNum = vertexNum;
    vexMaxNum = vertexMaxNum;
    arcNum = 0;
    infinity = infinit;
    tag = new Status[vexMaxNum];
    vexTable = new AdjListNetWorkVex<ElemType,
                                     WeightType>[vexMaxNum];
    for (int v = 0; v < vexNum; v++)
    {
        tag[v] = UNVISITED;
        vexTable[v].data = es[v];
        vexTable[v].firstarc = NULL;
    }
}
