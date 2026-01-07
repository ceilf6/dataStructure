// 每个节点保存孩子链表

typedef struct ChildNode
{
    int child;
    struct ChildNode *next;
} ChildNode;

typedef struct
{
    ElemType data;
    ChildNode *firstChild;
} CTNode;