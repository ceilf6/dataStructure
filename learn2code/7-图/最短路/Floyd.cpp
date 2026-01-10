#include "邻接表.h"

template <class ElemType, class WeightType>
void ShortestPathFloyd(const AdjListDirNetwork<ElemType,
                                               WeightType> &g,
                       int **path, WeightType **dist)
{
    for (int u = 0; u < g.GetVexNum(); u++)
        for (int v = 0; v < g.GetVexNum(); v++)
        {
            dist[u][v] = (u != v) ? g.GetWeight(u, v) : 0;
            if (u != v && dist[u][v] < g.GetInfinity())
                path[u][v] = u;
            else
                path[u][v] = -1;
        } // 矩阵A(-1)与path(-1)初始
    for (int k = 0; k < g.GetVexNum(); k++)
        for (int i = 0; i < g.GetVexNum(); i++)
            for (int j = 0; j < g.GetVexNum(); j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    path[i][j] = path[k][j];
                } // 缩短路径长度, 经过 k 到 j
}
