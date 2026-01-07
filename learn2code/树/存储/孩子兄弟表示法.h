/*
left → 第一个孩子
right → 下一个兄弟
*/

typedef struct CSNode
{
    ElemType data;
    struct CSNode *firstChild;
    struct CSNode *nextSibling;
} CSNode;