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
