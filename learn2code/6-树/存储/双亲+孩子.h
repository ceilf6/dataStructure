// 同时存父节点+孩子链表

typedef struct
{
    ElemType data;
    int parent;
    ChildNode *firstChild;
} PCTNode;