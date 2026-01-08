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
