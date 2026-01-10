// 辅助数组：对每个还不在 U 里的顶点 v 记录
template <class ElemType, class WeightType>
struct CloseArcType
{
    WeightType lowweight; // 当前生成树U 到该顶点的最小连接边权
    int nearvertex;       // U 中与该顶点最近（通过最小边连接）的那个顶点下标
};
