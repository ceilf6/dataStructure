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

// 求目标v的第一个邻接点序号：直接取顶点指向的adjVex
template <class ElemType, class WeightType>
int AdjListDirNetwork<ElemType, WeightType>::FirstAdjVex(int v) const
{
    if (v < 0 || v >= vexNum)
        throw Error("v不合法!"); // 抛出异常
    if (vexTable[v].firstarc == NULL)
        return -1; // 不存在邻接点
    else
        return vexTable[v].firstarc->adjVex;
}

// 下一个邻接点序号：利用 nextarc 的指向 adjVex
template <class ElemType, class WeightType>
int AdjListDirNetwork<ElemType, WeightType>::
    NextAdjVex(int v1, int v2) const
{
    AdjListNetworkArc<WeightType> *p;
    if (v1 < 0 || v1 >= vexNum)
        throw Error("v1不合法!");
    if (v2 < 0 || v2 >= vexNum)
        throw Error("v2不合法!");
    if (v1 == v2)
        throw Error("v1不能等于v2!");
    p = vexTable[v1].firstarc;           // 从 v1 的第一条边开始
    while (p != NULL && p->adjVex != v2) // 直到找到 v2
        p = p->nextarc;
    if (p == NULL || p->nextarc == NULL) // 这样后面的才是 v2 后面的第一个邻接点
        return -1;
    else
        return p->nextarc->adjVex;
}
