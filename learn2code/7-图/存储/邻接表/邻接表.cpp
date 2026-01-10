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

// 插入顶点：vexTable ，然后将新顶点指向的边节点信息初始化空
template <class ElemType, class WeightType>
void AdjListDirNetwork<ElemType, WeightType>::
    InsertVex(const ElemType &e)
{
    if (vexNum == vexMaxNum)
        throw Error("图的顶点数不能超过允许的最大数!");
    vexTable[vexNum].data = e;
    vexTable[vexNum].firstarc = NULL;
    tag[vexNum] = UNVISITED;
    vexNum++;
}

// 加入弧：从 v1 -> v2 的，那么只需要在 v1 后面添加新边节点信息，然后将原先的边节点信息接到新增节点后面
template <class ElemType, class WeightType>
void AdjListDirNetwork<ElemType, WeightType>::
    InsertArc(int v1, int v2, WeightType w)
{
    if (v1 < 0 || v1 >= vexNum)
        throw Error("v1不合法!");
    if (v2 < 0 || v2 >= vexNum)
        throw Error("v2不合法!");
    if (v1 == v2)
        throw Error("v1不能等于v2!");
    if (w == infinity)
        throw Error("w不能为无穷大!");
    AdjListNetworkArc<WeightType> *p, *q;
    p = vexTable[v1].firstarc;
    vexTable[v1].firstarc =
        new AdjListNetworkArc<WeightType>(v2, w, p);
    arcNum++;
}

// 删除弧：删除链表节点
template <class ElemType, class WeightType>
void AdjListDirNetwork<ElemType, WeightType>::
    DeleteArc(int v1, int v2)
{
    if (v1 < 0 || v1 >= vexNum)
        throw Error("v1不合法!");
    if (v2 < 0 || v2 >= vexNum)
        throw Error("v2不合法!");
    if (v1 == v2)
        throw Error("v1不能等于v2!");
    AdjListNetworkArc<WeightType> *p, *q;
    p = vexTable[v1].firstarc;
    while (p != NULL && p->adjVex != v2)
    {
        q = p;
        p = p->nextarc;
    }
    if (p != NULL)
    {
        if (vexTable[v1].firstarc == p)
            vexTable[v1].firstarc = p->nextarc;
        else
            q->nextarc = p->nextarc;
        delete p;
        arcNum--;
    }
}

// 删除顶点
/*
1. 删除“别人指向 v 的边”（入边）
2. 删除 v 自己的邻接边链表（出边）
3. 删除顶点并用最后一个顶点补位
4. 修正所有边结点里的 adjVex（下标修正）
*/
template <class ElemType, class WeightType>
void AdjListDirNetwork<ElemType, WeightType>::
    DeleteVex(const ElemType &d)
{
    int v;
    AdjListNetworkArc<WeightType> *p, *q;
    for (v = 0; v < vexNum; v++)
        if (vexTable[v].data == d)
            break;
    if (v == vexNum)
        throw Error("图中不存在要删除的顶点!");
    // 1. 删除“别人指向 v 的边”（入边）
    for (int u = 0; u < vexNum; u++)
        if (u != v)
            DeleteArc(u, v);
    p = vexTable[v].firstarc;
    // 2. 删除 v 自己的邻接边链表（出边）
    while (p != NULL)
    {
        vexTable[v].firstarc = p->nextarc;
        delete p;
        p = vexTable[v].firstarc;
        arcNum--;
    }
    // 3. 删除顶点并用最后一个顶点补位
    vexNum--;
    vexTable[v].data = vexTable[vexNum].data;
    vexTable[v].firstarc = vexTable[vexNum].firstarc;
    vexTable[vexNum].firstarc = NULL;
    tag[v] = tag[vexNum];
    // 4. 修正所有边结点里的 adjVex（下标修正）
    for (int u = 0; u < vexNum; u++)
        if (u != v)
        {
            p = vexTable[u].firstarc;
            while (p != NULL)
            {
                if (p->adjVex == vexNum)
                    p->adjVex = v;
                p = p->nextarc;
            }
        }
}
