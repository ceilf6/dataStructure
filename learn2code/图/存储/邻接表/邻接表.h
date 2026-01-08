#ifndef ADJACENCY_LIST_H
#define ADJACENCY_LIST_H

#include <cstddef>

template <class WeightType>
struct AdjListNetworkArc;

// 每个邻接表链表的头节点
template <class ElemType, class WeightType>
struct AdjListNetWorkVex
{
    ElemType data;                           // 顶点信息
    AdjListNetworkArc<WeightType> *firstarc; // 第一条边（头节点）

    AdjListNetWorkVex() : firstarc(NULL) {}
    AdjListNetWorkVex(ElemType val,
                      AdjListNetworkArc<WeightType> *adj = NULL)
        : data(val), firstarc(adj) {}
};

// 邻接表中每一条边的节点结构
template <class WeightType>
struct AdjListNetworkArc
{
    int adjvex;                             // 顶点数组中的下标，标识这条边是连向哪个顶点
    WeightType weight;                      // 边权值
    AdjListNetworkArc<WeightType> *nextarc; // 指向同一顶点的下一条边

    AdjListNetworkArc(int v,
                      WeightType w,
                      AdjListNetworkArc *n = NULL)
        : adjvex(v), weight(w), nextarc(n) {}
};

/*
AdjListNetWorkVex vertexes[vexNum];

vertexes[0] --> arc0_1 -> arc0_2 -> arc0_3 -> NULL
vertexes[1] --> arc1_1 -> arc1_2 -> NULL
vertexes[2] --> NULL
...
*/
// 有向图邻接表类
template <class ElemType, class WeightType>
class AdjListDirNetwork
{
protected:
    int vexNum, vexMaxNum, arcNum;
    AdjListNetWorkVex<ElemType, WeightType> *vexTable;
    mutable Status *tag;
    WeightType infinity;

public:
    AdjListDirNetwork(ElemType es[], int vertexNum,
                      int vertexMaxNum = DEFAULT_SIZE,
                      WeightType infinit = (WeightType)DEFAULT_INFINITY);
    AdjListDirNetwork(int vertexMaxNum = DEFAULT_SIZE,
                      WeightType infinit = (WeightType)DEFAULT_INFINITY);
    ~AdjListDirNetwork();
    void Clear();
    bool IsEmpty();
    int GetOrder(ElemType &d) const;
    Status GetElem(int v, ElemType &e) const;
    Status SetElem(int v, const ElemType &d);
    WeightType GetInfinity() const;
    int GetVexNum() const;
    int GetArcNum() const;
    int FirstAdjVex(int v) const;
    int NextAdjVex(int v1, int v2) const;
    void InsertVex(const ElemType &d);
    void InsertArc(int v1, int v2, WeightType w);
    void DeleteVex(const ElemType &d);
    void DeleteArc(int v1, int v2);
    WeightType GetWeight(int v1, int v2) const;
    void SetWeight(int v1, int v2, WeightType w);
    Status GetTag(int v) const;
    void SetTag(int v, Status tag) const;
    AdjListDirNetwork(const AdjListDirNetwork<ElemType,
                                              WeightType> &copy);
    AdjListDirNetwork<ElemType, WeightType> &operator=(const AdjListDirNetwork<ElemType, WeightType>
                                                           &copy);
    void Display();
};

#endif
