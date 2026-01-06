#include "双向链表.h"

// 1. 构造函数：构造空双向链表
template <class ElemType>
DblLinkList<ElemType>::DblLinkList()
{
    head = new DblNode<ElemType>;
    assert(head);
    head->prior = head->next = head;
    length = 0;
}

// 2. 数组转双向链表
template <class ElemType>
DblLinkList<ElemType>::DblLinkList(ElemType v[], int n)
{
    DblNode<ElemType> *p;
    p = head = new DblNode<ElemType>;
    assert(head);
    for (int i = 0; i < n; i++)
    {
        p->next = new DblNode<ElemType>(v[i], p);
        p = p->next;
    }
    length = n;
    head->prior = p;
    p->next = head;
}

// 3. 析构函数
template <class ElemType>
DblLinkList<ElemType>::~DblLinkList()
{
    Clear(); // 调用清除函数
    delete head;
}

template <class ElemType>
void DblLinkList<ElemType>::Clear()
{
    ElemType tmpElem;
    while (length > 0)
        DeleteElem(1, tmpElem); // 调用删除节点函数
}

// 遍历并应用函数
template <class ElemType>
void DblLinkList<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
{
    DblNode<ElemType> *p;
    for (p = head->next; p != head; p = p->next)
        (*Visit)(p->data);
}

// 找节点
template <class ElemType>
int DblLinkList<ElemType>::LocateElem(const ElemType &e)
{
    DblNode<ElemType> *p = head->next;
    int count = 1;
    while (p != head && p->data != e) // 双向中用 !=head 防止环
    {
        count++;
        p = p->next;
    }
    if (p != head)
        return count;
    else
        return 0;
}

// 取指定的第 i 个元素
template <class ElemType>
DblLinkList<ElemType>::Status DblLinkList<ElemType>::GetElem(int i, ElemType &e) const
{
    DblNode<ElemType> *p = head->next;
    int count;
    if (i < 1 || i > length)
        return NOT_PRESENT;
    else
    {
        for (count = 1; count < i; count++)
            p = p->next;
        e = p->data;
        return ENTRY_FOUND;
    }
}

// 修改元素
template <class ElemType>
DblLinkList<ElemType>::Status DblLinkList<ElemType>::SetElem(int i, const ElemType &e)
{
    DblNode<ElemType> *p = head->next;
    int count;
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        for (count = 1; count < i; count++)
            p = p->next;
        p->data = e;
        return SUCCESS;
    }
}

// 删除节点
template <class ElemType>
DblLinkList<ElemType>::Status DblLinkList<ElemType>::DeleteElem(int i, ElemType &e)
{
    DblNode<ElemType> *p = head->next;
    int count;
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        for (count = 1; count < i; count++)
            p = p->next;
        p->prior->next = p->next;
        p->next->prior = p->prior;
        e = p->data;
        length--;
        delete p;
        return SUCCESS;
    }
}

// 插入元素
template <class ElemType>
DblLinkList<ElemType>::Status DblLinkList<ElemType>::InsertElem(int i, const ElemType &e)
{
    DblNode<ElemType> *p = head->next, *q;
    int count;
    if (i < 1 || i > length + 1)
        return RANGE_ERROR;
    else
    {
        for (count = 1; count < i; count++)
            p = p->next;
        q = new DblNode<ElemType>(e, p->prior, p);
        p->prior->next = q;
        p->prior = q;
        length++;
        return SUCCESS;
    }
}

// 默认在表尾插入
template <class ElemType>
DblLinkList<ElemType>::Status DblLinkList<ElemType>::InsertElem(const ElemType &e)
{
    DblNode<ElemType> *p;
    p = new DblNode<ElemType>(e, head->prior, head);
    head->prior->next = p;
    head->prior = p;
    length++;
    return SUCCESS;
}