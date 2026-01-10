// 和邻接表一样也是 顶点节点 和 弧节点

template <class ElemType>
struct VexNode
{
    ElemType data;     // 顶点数据
    ArcNode *firstout; // 第一条出边
    ArcNode *firstin;  // 第一条入边
};

template <class WeightType>
struct ArcNode
{
    int tailvex;       // 弧尾（起点）下标
    int headvex;       // 弧头（终点）下标
    ArcNode *tlink;    // 下一条“同起点”的边
    ArcNode *hlink;    // 下一条“同终点”的边
    WeightType weight; // 边权（可选）
};

/*
找某顶点的出边
for (ArcNode* p = vex[v].firstout; p != NULL; p = p->tlink)
{
    // v -> p->headvex
}

找某顶点的入边!
for (ArcNode* p = vex[v].firstin; p != NULL; p = p->hlink)
{
    // p->tailvex -> v
}
*/