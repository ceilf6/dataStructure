// 记录父节点下标

typedef struct
{
    ElemType data;
    int parent; // 父结点在数组中的下标，根结点为 -1
} PTNode;

PTNode tree[MAXSIZE];