#include "邻接表.h"

template <class ElemType, class WeightType>
void ShortestPathBellmanFord(const AdjListDirNetwork<ElemType,
                                                     WeightType> &g,
                             int v0, int *path, WeightType *dist)
{
    WeightType *distTemp, minVal, infinity = g.GetInfinity();
    int v, u, vexNum = g.GetVexNum();
    distTemp = new WeightType[vexNum];
    for (v = 0; v < vexNum; v++)
    { // 初始化path和dist
        dist[v] = (v0 != v) ? g.GetWeight(v0, v) : 0;
        if (dist[v] == infinity)
            path[v] = -1;
        else
            path[v] = v0;
    }
    for (int k = 2; k < vexNum; k++)
    {
        for (v = 0; v < vexNum; v++)
            distTemp[v] = dist[v];
        for (u = 0; u < vexNum; u++)
            if (u != v0)
                for (v = 0; v < vexNum; v++)
                    if (v != v0 && distTemp[u] > dist[v] + g.GetWeight(v, u))
                    {
                        distTemp[u] = dist[v] + g.GetWeight(v, u);
                        path[u] = v;
                    }
        for (v = 0; v < vexNum; v++)
            dist[v] = distTemp[v];
    }
}
