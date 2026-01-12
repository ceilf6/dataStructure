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

// 7. 取第 i 个元素值到 e 中
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
        // 让指针 p 指向和 head 指向的同一个节点
        /* 相当于
        Node<ElemType>* p = head;
        Node<ElemType>* q;   // 只是声明，还没指向任何地方
        */
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

// 通过递归实现链表反转
/*
也就是这三步反复发生：
    1.	递归反转 p->next 之后的链表
    2.	让 p->next->next = p
    3.	断开 p->next
*/
template <class ElemType>
void LinkList<ElemType>::reverse(Node<ElemType> *head) const
{
    // 边界：空结点或最后一个结点
    if (head == nullptr || head->next == nullptr)
        return head;

    Node<ElemType> *last = reverse(head->next);

    // 反转
    head->next->next = head;
    head->next = nullptr; // succesor
    // 必须每次都接到 nullptr 上，否则会形成环
    /*
    1 → 2 → 1 → 2 → ...
        ↑     ↓
        └─────┘
    */

    return last;
    // last 不会变，永远是原链表反转区间的尾，也就是新链表的头
}

// 非递归实现链表反转
/*
逐个把 next 指针反向
*/
template <class ElemType>
Node<ElemType> *ReverseIter(Node<ElemType> *head)
{
    Node<ElemType> *prev = nullptr;
    Node<ElemType> *cur = head;
    Node<ElemType> *next = nullptr;

    while (cur != nullptr)
    {
        next = cur->next; // ① 先保存后继
        cur->next = prev; // ② 翻转指针
        prev = cur;       // ③ prev 前进
        cur = next;       // ④ cur 前进
    }

    return prev; // 新头结点
}