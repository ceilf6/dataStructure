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

// 带权
template <class ElemType, class WeightType>
class AdjMatrixUndirNetwork // 不能继承，因为 AdjMatrixUndirGraph 中的 arcs 是用的 0/1
{
protected:
    int vexNum, vexMaxNum, arcNum;
    WeightType **arcs;   // 邻接矩阵（权值）
    ElemType *vertexes;  // 顶点信息
    mutable Status *tag; // 访问标记
    WeightType infinity; // 表示“不连通”的无穷大

public:
    // 构造 / 析构
    AdjMatrixUndirNetwork(ElemType es[], int vertexNum,
                          int vertexMaxNum = DEFAULT_SIZE,
                          WeightType inf = INF);
    AdjMatrixUndirNetwork(int vertexMaxNum = DEFAULT_SIZE,
                          WeightType inf = INF);
    ~AdjMatrixUndirNetwork();

    void Clear();
    bool IsEmpty() const;

    // 顶点相关
    int GetOrder(ElemType &d) const;
    Status GetElem(int v, ElemType &d) const;
    int GetVexNum() const;
    int GetArcNum() const;

    // 边相关（网络特有）
    WeightType GetWeight(int v1, int v2) const;
    WeightType GetInfinity() const { return infinity; }

    // 邻接点
    int FirstAdjVex(int v) const;
    int NextAdjVex(int v1, int v2) const;

    // 修改操作
    void InsertVex(const ElemType &d);
    void InsertArc(int v1, int v2, WeightType w);
    void DeleteVex(const ElemType &d);
    void DeleteArc(int v1, int v2);

    // 遍历辅助
    Status GetTag(int v) const;
    void SetTag(int v, Status val) const;

    void Display() const;
};