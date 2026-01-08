#include "Prim.h"
#include "邻接矩阵.h"

// “加点法”

template <class ElemType, class WeightType>
void MiniSpanTreePrim(const AdjMatrixUndirNetwork<ElemType,
                                                  WeightType> &g,
                      int u0)
{
    WeightType min;
    ElemType v1, v2;
    int vexnum = g.GetVexNum();
    CloseArcType<ElemType, WeightType> *closearc;
    if (u0 < 0 || u0 >= vexnum)
        throw Error("顶点u0不存在!");
    int u, v, k;
    closearc = new CloseArcType<ElemType, WeightType>[vexnum];
    // 初始化U={u0}
    for (v = 0; v < vexnum; v++)
    {
        closearc[v].nearvertex = u0;
        closearc[v].lowweight = g.GetWeight(u0, v);
    }
    closearc[u0].nearvertex = -1;
    closearc[u0].lowweight = 0;
    // 主循环：每次将一个新顶点加入 U
    for (k = 1; k < vexnum; k++)
    {
        min = g.GetInfinity();
        v = u0;
        // 在所有未加入的顶点中找最小边权 lowweight
        // Prim 的贪心：选一条当前最便宜的“横切边”(U, V-U)
        for (u = 0; u < vexnum; u++)
            if (closearc[u].lowweight != 0 && closearc[u].lowweight < min)
            {
                v = u;
                min = closearc[u].lowweight;
            }
        // 加入
        if (v != u0)
        {
            g.GetElem(closearc[v].nearvertex, v1);
            g.GetElem(v, v2);
            cout << "边:( " << v1 << ", " << v2 << " ) 权:" << min << endl;
            closearc[v].lowweight = 0;
            // 用新加入的顶点 v 去“松弛更新”其他点的最小连接边
            for (u = g.FirstAdjVex(v); u != -1; u = g.NextAdjVex(v, u))
                if (closearc[u].lowweight != 0 &&
                    (g.GetWeight(v, u) < closearc[u].lowweight))
                {
                    closearc[u].lowweight = g.GetWeight(v, u);
                    closearc[u].nearvertex = v;
                }
        }
    }
    delete[] closearc;
}
