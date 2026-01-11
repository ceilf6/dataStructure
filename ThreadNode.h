typedef struct ThreadNode
{
    int data;
    struct ThreadNode *lchild, *rchild, *parent;
    int ltag, rtag;
} ThreadNode;