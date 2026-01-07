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
