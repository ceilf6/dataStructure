#include "邻接表.h"

// 双重循环 O(n**2)

template <class ElemType, class WeightType>
void ShortestPathDij(const AdjListDirNetwork<ElemType, WeightType> &g, int v0, int *path, WeightType *dist)
{
    WeightType minVal, infinity = g.GetInfinity();
    int v, u;
    for (v = 0; v < g.GetVexNum(); v++)
    {
        dist[v] = g.GetWeight(v0, v);
        if (dist[v] == infinity)
            path[v] = -1;
        else
            path[v] = v0;
        g.SetTag(v, UNVISITED);
    }
    g.SetTag(v0, VISITED);
    for (int i = 1; i < g.GetVexNum(); i++)
    {
        minVal = infinity;
        u = v0;
        for (v = 0; v < g.GetVexNum(); v++)
            if (g.GetTag(v) == UNVISITED && dist[v] < minVal)
            {
                u = v;
                minVal = dist[v];
            }
        g.SetTag(u, VISITED);
        for (v = g.FirstAdjVex(u); v != -1; v = g.NextAdjVex(u, v))
            if (g.GetTag(v) == UNVISITED &&
                minVal + g.GetWeight(u, v) < dist[v])
            {
                dist[v] = minVal + g.GetWeight(u, v);
                path[v] = u;
            }
    }
}
