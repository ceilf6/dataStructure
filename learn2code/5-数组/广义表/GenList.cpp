#include "GenList.h"

template <class ElemType>
int GenList<ElemType>::DepthHelp(const GenListNode<ElemType> *hd)
// 通过递归得到以hd为表头的广义表的深度
{
    if (hd->tLink == NULL)
        return 1;
    int subMaxDepth = 0; // 子表最大深度
    for (GenListNode<ElemType> *p = hd->tLink; p != NULL; p = p->tLink)
    {
        if (p->tag == LIST) // LIST -> 子表
        {
            int curSubDepth = DepthHelp(p->hLink); // 递归拿到子表深度
            if (subMaxDepth < curSubDepth)
                subMaxDepth = curSubDepth;
        }
    }
    return subMaxDepth + 1; // 注意要加1
}

template <class ElemType>
void GenList<ElemType>::ClearHelp(GenListNode<ElemType> *hd)
{
    // 操作结果：释放以hd为表头的广义表结构
    hd->ref--;
    if (hd->ref == 0)
    {
        GenListNode<ElemType> *pre = hd, *p;
        for (p = hd->tLink; p != NULL; p = p->tLink)
        {
            delete pre;
            pre = p;
            if (p->tag == LIST)
                ClearHelp(p->hLink); // 递归释放子表
        }
        delete pre;
    }
}

template <class ElemType>
void GenList<ElemType>::CopyHelp(const GenListNode<ElemType> *sourceHead,
                                 GenListNode<ElemType> *&destHead)
{
    destHead = new GenListNode<ElemType>(HEAD);
    GenListNode<ElemType> *destPtr = destHead;
    destHead->ref = 1;
    for (GenListNode<ElemType> *p = sourceHead->tLink; p != NULL;
         p = p->tLink)
    {
        destPtr = destPtr->tLink = new GenListNode<ElemType>(p->tag);
        if (p->tag == LIST)
            CopyHelp(p->hLink, destPtr->hLink); // 递归复制子表
        else
            destPtr->atom = p->atom;
    }
}

// 比较两个广义表是否相等（结构和内容完全相同）
// 返回：1 相等，0 不相等
template <class ElemType>
int CmpHelp(const GenListNode<ElemType> *hd1, const GenListNode<ElemType> *hd2)
{
    // 两个都是空表
    if (hd1->tLink == NULL && hd2->tLink == NULL)
        return 1;

    // 一个空一个非空
    if (hd1->tLink == NULL || hd2->tLink == NULL)
        return 0;

    // 双指针同步遍历两个表的元素
    GenListNode<ElemType> *p1 = hd1->tLink;
    GenListNode<ElemType> *p2 = hd2->tLink;

    while (p1 != NULL && p2 != NULL)
    {
        // tag 类型不同
        if (p1->tag != p2->tag)
            return 0;

        if (p1->tag == ATOM)
        {
            // 原子节点：比较值
            if (p1->atom != p2->atom)
                return 0;
        }
        else // p1->tag == LIST
        {
            // 表节点：递归比较子表
            if (!CmpHelp(p1->hLink, p2->hLink))
                return 0;
        }

        p1 = p1->tLink;
        p2 = p2->tLink;
    }

    // 长度不同（一个遍历完了，另一个还有）
    if (p1 != NULL || p2 != NULL)
        return 0;

    return 1;
}