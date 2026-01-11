// 线索化之后就不需要依赖栈递归
// 其中中序线索二叉树遍历最为简单，后序线索二叉树由于其后继结点与父结点及左右子树关系密切，通常需要借助父指针或额外结构才能完成遍历。

// 中序
ThreadNode *FirstNode(ThreadNode *p)
{
    while (p->ltag == 0)
        p = p->lchild;
    return p;
}
ThreadNode *NextNode(ThreadNode *p)
{
    if (p->rtag == 1)
        return p->rchild; // 线索，直接后继
    else
    {
        p = p->rchild; // 右子树
        while (p->ltag == 0)
            p = p->lchild;
        return p;
    }
}
void InOrder(ThreadNode *T)
{
    for (ThreadNode *p = FirstNode(T); p != NULL; p = NextNode(p))
        visit(p);
}

// 先序
/*
有左孩子就先访问左孩子
没有左孩子就顺着后继线索走
*/
ThreadNode *PreNextNode(ThreadNode *p)
{
    if (p->ltag == 0)
        return p->lchild;
    else
        return p->rchild;
}
void PreOrder(ThreadNode *T)
{
    for (ThreadNode *p = T; p != NULL; p = PreNextNode(p))
        visit(p);
}

// 后序
ThreadNode *PostFirstNode(ThreadNode *p)
{
    while (p->ltag == 0 || p->rtag == 0)
    {
        if (p->ltag == 0)
            p = p->lchild;
        else
            p = p->rchild;
    }
    return p;
}
ThreadNode *PostNextNode(ThreadNode *p)
{
    if (p->rtag == 1)
        return p->rchild; // 线索直接后继

    ThreadNode *parent = p->parent;

    if (parent == NULL)
        return NULL;

    if (parent->rtag == 0 && parent->rchild != p)
        return PostFirstNode(parent->rchild);
    else
        return parent;
}
void PostOrder(ThreadNode *T)
{
    for (ThreadNode *p = PostFirstNode(T); p != NULL; p = PostNextNode(p))
        visit(p);
}