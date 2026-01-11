#include "邻接矩阵.h"

// 邻接矩阵 O(n**2)

/*
tag 的作用就相当于一个 vis 集合
    所以在递归部分需要 g.GetTag(w) == UNVISITED 判断
*/

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
        // 遍历邻接节点
        if (g.GetTag(w) == UNVISITED)
            DFS(g, w, Visit);
}

// 整图DFS遍历（处理图是非连通的情况）
template <class ElemType>
void DFSTraverse(const AdjMatrixUndirGraph<ElemType> &g,
                 void (*Visit)(const ElemType &))
{
    // 遍历子图
    int v;
    for (v = 0; v < g.GetVexNum(); v++)
        g.SetTag(v, UNVISITED);
    for (v = 0; v < g.GetVexNum(); v++)
        if (g.GetTag(v) == UNVISITED)
            DFS(g, v, Visit);
}

/*
深度优先遍历(模拟栈实现)
算法伪代码：
1. 栈初始化;
2. 输出起始顶点a，并改为" 已访问 "标识；将a进栈;
3. 重复下列操作直到栈为空：
   3.1. 取栈顶元素顶点（不出栈）;
   3.2. 栈顶元素顶点存在未被访问过的邻接点W，则
     3.2.1. 输出顶点 W;
     3.2.2. 将顶点W改为“已访问”  标志;
     3.2.3. 将顶点W进栈;
   3.3. 否则 当前顶点退栈;
*/