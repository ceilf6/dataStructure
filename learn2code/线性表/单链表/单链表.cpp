#include "单链表.h"

// 1. 空链表
template <class ElemType>
LinkList<ElemType>::LinkList()
{
    head = new Node<ElemType>;
    assert(head);
    length = 0;
}
// 2. 数组转链表
template <class ElemType>
LinkList<ElemType>::LinkList(ElemType v[], int n)
{
    Node<ElemType> *p;
    p = head = new Node<ElemType>;
    assert(head);
    for (int i = 0; i < n; i++)
    {
        p->next = new Node<ElemType>(v[i], NULL);
        assert(p->next);
        p = p->next;
    }
    length = n;
}
// 3. 析构函数
template <class ElemType>
LinkList<ElemType>::~LinkList()
{
    Clear(); // 4. 遍历销毁节点
    delete head;
}

template <class ElemType>
void LinkList<ElemType>::Clear()
{
    Node<ElemType> *p = head->next;
    while (p != NULL)
    {
        head->next = p->next;
        delete p;
        p = head->next;
    }
    length = 0;
}

// 5. 遍历并作用
template <class ElemType>
void LinkList<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
{
    Node<ElemType> *p = head->next;
    while (p != NULL)
    {
        (*Visit)(p->data);
        p = p->next;
    }
}

// 6. 定位第几个元素
template <class ElemType>
int LinkList<ElemType>::LocateElem(const ElemType &e) const
{
    Node<ElemType> *p = head->next;
    int count = 1;
    while (p != NULL && p->data != e)
    {
        count++;
        p = p->next;
    }
    return (p != NULL) ? count : 0;
}

// 7. 取第几个元素值
template <class ElemType>
LinkList<ElemType>::Status LinkList<ElemType>::GetElem(int i, ElemType &e) const
{
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        Node<ElemType> *p = head->next;
        int count;
        for (count = 1; count < i; count++)
            p = p->next;
        e = p->data;
        return ENTRY_FOUND;
    }
}

// 8. 设第几个元素值
template <class ElemType>
LinkList<ElemType>::Status LinkList<ElemType>::SetElem(int i, const ElemType &e)
{
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        Node<ElemType> *p = head->next;
        int count;
        for (count = 1; count < i; count++)
            p = p->next;
        p->data = e;
        return SUCCESS;
    }
}

// 9. 删除第几个元素
template <class ElemType>
LinkList<ElemType>::Status LinkList<ElemType>::DeleteElem(int i, ElemType &e)
{
    if (i < 1 || i > length)
        return RANGE_ERROR;
    else
    {
        Node<ElemType> *p = head, *q;
        int count;
        for (count = 1; count < i; count++)
            p = p->next;
        q = p->next;
        p->next = q->next;
        e = q->data;
        length--;
        delete q; // 对被跳过的、标记的指针删除
        return SUCCESS;
    }
}

// 10. 插入元素
template <class ElemType>
LinkList<ElemType>::Status LinkList<ElemType>::InsertElem(int i, const ElemType &e)
{
    if (i < 1 || i > length + 1)
        return RANGE_ERROR;
    else
    {
        Node<ElemType> *p = head, *q;
        int count;
        for (count = 1; count < i; count++)
            p = p->next;
        q = new Node<ElemType>(e, p->next);
        assert(q);
        p->next = q;
        length++;
        return SUCCESS;
    }
}

// 11. 在末尾插入
template <class ElemType>
LinkList<ElemType>::Status LinkList<ElemType>::InsertElem(const ElemType &e)
{
    Node<ElemType> *p, *q;
    q = new Node<ElemType>(e, NULL);
    assert(q);
    for (p = head; p->next != NULL; p = p->next)
        ;
    p->next = q;
    length++;
    return SUCCESS;
}
