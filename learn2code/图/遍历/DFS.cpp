#include "邻接矩阵.h"

// 邻接矩阵 O(n**2)

// 单源DFS
template <class ElemType>
void DFS(const AdjMatrixUndirGraph<ElemType> &g,
         int v, void (*Visit)(const ElemType &))
{
    ElemType e;
    g.SetTag(v, VISITED);
    g.GetElem(v, e);
    Visit(e);
    for (int w = g.FirstAdjVex(v); w != -1;
         w = g.NextAdjVex(v, w))
        if (g.GetTag(w) == UNVISITED)
            DFS(g, w, Visit);
}

// 整图DFS遍历（处理图是非连通的情况）
template <class ElemType>
void DFSTraverse(const AdjMatrixUndirGraph<ElemType> &g,
                 void (*Visit)(const ElemType &))
{
    int v;
    for (v = 0; v < g.GetVexNum(); v++)
        g.SetTag(v, UNVISITED);
    for (v = 0; v < g.GetVexNum(); v++)
        if (g.GetTag(v) == UNVISITED)
            DFS(g, v, Visit);
}
