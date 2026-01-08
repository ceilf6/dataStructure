#include "Status.h"
#include "邻接表.h"

template <class ElemType, class WeightType>
Status CriticalPath(const AdjListDirNetwork<ElemType, WeightType> &g)
{
    int *indegree = new int[g.GetVexNum()];
    WeightType *ve = new int[g.GetVexNum()]; // 事件最早发生
    WeightType *vl = new int[g.GetVexNum()]; // 事件最迟发生
    LinkQueue<int> q;
    LinkStack<int> s; // 用于获取拓扑逆序
    int ee, el, u, v, count = 0;
    ElemType e1, e2;
    for (v = 0; v < g.GetVexNum(); v++)
        ve[v] = 0;
    StatIndegree(g, indegree);
    for (v = 0; v < g.GetVexNum(); v++)
        if (indegree[v] == 0)
            q.EnQueue(v);
    while (!q.IsEmpty())
    {
        q.DelQueue(u);
        s.Push(u);
        count++;
        for (v = g.FirstAdjVex(u); v != -1; v = g.NextAdjVex(u, v))
        {
            if (--indegree[v] == 0)
                q.EnQueue(v);
            if (ve[u] + g.GetWeight(u, v) > ve[v]) // 拓扑序计算ve
                ve[v] = ve[u] + g.GetWeight(u, v);
        }
    }
    delete[] indegree;
    if (count < g.GetVexNum())
    {
        delete[] ve;
        delete[] vl;
        return FAIL; // 网g有回路
    }
    s.Top(u); // 取出栈顶u,为汇点
    for (v = 0; v < g.GetVexNum(); v++)
        vl[v] = ve[u];
    while (!s.IsEmpty())
    {
        s.Pop(u); // 计算vl,事件最晚
        for (v = g.FirstAdjVex(u); v != -1; v = g.NextAdjVex(u, v))
            if (vl[v] - g.GetWeight(u, v) < vl[u])
                vl[u] = vl[v] - g.GetWeight(u, v);
    }
    for (u = 0; u < g.GetVexNum(); u++)
    {
        for (v = g.FirstAdjVex(u); v != -1; v = g.NextAdjVex(u, v))
        {
            ee = ve[u];
            el = vl[v] - g.GetWeight(u, v);
            if (ee == el)
            {
                g.GetElem(u, e1);
                g.GetElem(v, e2);
                cout << "<" << e1 << ", " << e2 << "> ";
            } // 通过计算活动最早ee,活动最晚el,得到关键活动。
        }
    }
    delete[] ve;
    delete[] vl;
    return SUCCESS;
}
