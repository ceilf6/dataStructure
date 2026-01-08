#include "邻接矩阵.h"

// 构造函数-初始化邻接矩阵
template <class ElemType>
AdjMatrixUndirGraph<ElemType>::AdjMatrixUndirGraph(int vertexMaxNum)
{
    if (vertexMaxNum < 0)
        throw Error("允许的顶点最大数目不能为负!");
    vexNum = 0;
    vexMaxNum = vertexMaxNum;
    arcNum = 0;
    vertexes = new ElemType[vexMaxNum];
    tag = new Status[vexMaxNum];
    arcs = (int **)new int *[vexMaxNum]; // 行数
    for (int v = 0; v < vexMaxNum; v++)
        arcs[v] = new int[vexMaxNum]; // 列数
}

// 带点信息的构造函数
template <class ElemType>
AdjMatrixUndirGraph<ElemType>::AdjMatrixUndirGraph(ElemType es[],
                                                   int vertexNum, int vertexMaxNum)
{
    if (vertexMaxNum < 0)
        throw Error("允许的顶点最大数目不能为负!");
    if (vertexMaxNum < vertexNum)
        throw Error("顶点数目不能大于允许的顶点最大数目!");
    vexNum = vertexNum;
    vexMaxNum = vertexMaxNum;
    arcNum = 0;
    vertexes = new ElemType[vexMaxNum];
    tag = new Status[vexMaxNum];
    arcs = (int **)new int *[vexMaxNum];
    for (int v = 0; v < vexMaxNum; v++)
        arcs[v] = new int[vexMaxNum];
    for (int v = 0; v < vexNum; v++)
    {
        vertexes[v] = es[v];
        tag[v] = UNVISITED;
        for (int u = 0; u < vexNum; u++)
            arcs[v][u] = 0;
    }
}

// 找第一个邻接点序号
// 在所有与目标 v 顶点直接相连的顶点中按索引顺序找到第一个相邻顶点的下标
template <class ElemType>
int AdjMatrixUndirGraph<ElemType>::FirstAdjVex(int v) const
{
    if (v < 0 || v >= vexNum)
        throw Error("v不合法!");
    for (int u = 0; u < vexNum; u++)
        if (arcs[v][u] != 0)
            return u;
    return -1;
}

// 求目标 v1 从 v2 开始（不包括v2）下一个邻接点序号
template <class ElemType>
int AdjMatrixUndirGraph<ElemType>::NextAdjVex(int v1,
                                              int v2) const
{
    if (v1 < 0 || v1 >= vexNum)
        throw Error("v1不合法!");
    if (v2 < 0 || v2 >= vexNum)
        throw Error("v2不合法!");
    if (v1 == v2)
        throw Error("v1不能等于v2!");
    for (int u = v2 + 1; u < vexNum; u++)
        if (arcs[v1][u] != 0)
            return u;
    return -1;
}

// 插入顶点
template <class ElemType>
void AdjMatrixUndirGraph<ElemType>::InsertVex(const ElemType &d)
{
    if (vexNum == vexMaxNum)
        throw Error("图的顶点数不能超过允许的最大数!");
    vertexes[vexNum] = d;
    tag[vexNum] = UNVISITED;          // 打标记新点在图的遍历中没有被访问过
    for (int v = 0; v <= vexNum; v++) // 初始化无边
    {
        arcs[vexNum][v] = 0;
        arcs[v][vexNum] = 0;
    }
    vexNum++;
}

// 插入边：在邻接矩阵对应位置（无向图是对称的两处）打标记
template <class ElemType>
void AdjMatrixUndirGraph<ElemType>::InsertArc(int v1,
                                              int v2)
{
    if (v1 < 0 || v1 >= vexNum)
        throw Error("v1不合法!");
    if (v2 < 0 || v2 >= vexNum)
        throw Error("v2不合法!");
    if (v1 == v2)
        throw Error("v1不能等于v2!");
    if (arcs[v1][v2] == 0)
    {
        arcNum++;
        arcs[v1][v2] = 1;
        arcs[v2][v1] = 1;
    }
}
