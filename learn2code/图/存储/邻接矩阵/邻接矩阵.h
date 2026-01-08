template <class ElemType>
class AdjMatrixUndirGraph
{
protected:
    int vexNum, vexMaxNum, arcNum;
    /*
    vexNum: 图中实际存在的顶点个数
    vexMaxNum: 图中最多允许的顶点数（矩阵容量上限）
    arcNum: 当前图中边（弧）的条数
        在无向图中新增一条边虽然邻接矩阵对称两个地方都要存储，但是 arcNum 只加1
    */
    int **arcs; // 二维矩阵
    /*
    无权图：
    arcs[i][j] = 1; // 有边
    arcs[i][j] = 0; // 无边
    带权图：
    arcs[i][j] = w;   // 权值
    arcs[i][j] = INF; // 不连通
    */
    ElemType *vertexes; // 顶点信息，例如 'A'点
    mutable Status *tag;
    /*
    是否访问过
    tag[i] == UNVISITED
    tag[i] == VISITED

    通过设置为 mutable 即使在 const 成员函数中也允许修改 tag，图本身结构不变但在遍历时，访问标记作为算法临时状态
    */

public:
    AdjMatrixUndirGraph(ElemType es[], int vertexNum,
                        int vertexMaxNum = DEFAULT_SIZE);
    AdjMatrixUndirGraph(int vertexMaxNum = DEFAULT_SIZE);
    ~AdjMatrixUndirGraph();
    void Clear();
    bool IsEmpty();
    int GetOrder(ElemType &d) const;
    Status GetElem(int v, ElemType &d) const;
    Status SetElem(int v, const ElemType &d);
    int GetVexNum() const;
    int GetArcNum() const;
    int FirstAdjVex(int v) const;
    int NextAdjVex(int v1, int v2) const;
    void InsertVex(const ElemType &d);
    void InsertArc(int v1, int v2);
    void DeleteVex(const ElemType &d);
    void DeleteArc(int v1, int v2);
    Status GetTag(int v) const;
    void SetTag(int v, Status val) const;
    AdjMatrixUndirGraph(const AdjMatrixUndirGraph<ElemType> &g);
    AdjMatrixUndirGraph<ElemType> &operator=(
        const AdjMatrixUndirGraph<ElemType> &g);
    void Display();
};
