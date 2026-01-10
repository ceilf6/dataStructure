#include "邻接表.h"
#include "Status.h"

// 基于入度的拓扑排序

// 统计入度
template <class ElemType>
void StatIndegree(const AdjListDirGraph<ElemType> &g,
                  int *indegree)
{
    for (int v = 0; v < g.GetVexNum(); v++)
        indegree[v] = 0;
    // 建立入度表：将入度为0的点入栈
    for (int v = 0; v < g.GetVexNum(); v++)
        for (int u = g.FirstAdjVex(v); u != -1;
             u = g.NextAdjVex(v, u))
            indegree[u]++;
}

template <class ElemType>
Status TopSort(const AdjListDirGraph<ElemType> &g)
{
    int *indegree = new int[g.GetVexNum()];
    int v, u, count = 0, top = -1;
    ElemType e;
    StatIndegree(g, indegree);
    for (v = 0; v < g.GetVexNum(); v++)
        if (indegree[v] == 0)
        { // 入度为0的顶点入栈
            indegree[v] = top;
            top = v;
        }
    // 栈非空就不断弹
    while (top != -1)
    {
        v = top;
        top = indegree[v];
        g.GetElem(v, e);
        cout << e << " "; // 栈顶元素出栈并输出
        count++;
        // 扫描以顶点 v 为弧尾的所有弧：降低后继顶点的入度（PPT中说错了）
        for (u = g.FirstAdjVex(v); u != -1; u = g.NextAdjVex(v, u))
            if (--indegree[u] == 0)
            { // u入度减1,为0则入栈
                indegree[u] = top;
                top = u;
            }
    } // 继续拓扑排序
    delete[] indegree;
    // 判断是否有环
    if (count < g.GetVexNum())
        return FAIL; // 图g有回路
    else
        return SUCCESS; // 拓扑排序成功
}
