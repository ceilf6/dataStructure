#ifndef __LINK_STACK_H__
#define __LINK_STACK_H__

#include "Assistance.h" // 辅助软件包
#include "Node.h"       // 结点类

// 链栈类（带头结点）
template <class ElemType>
class LinkStack
{
protected:
    //  链栈的数据成员
    Node<ElemType> *head; // 头结点指针
    int length;           // 栈中元素个数

public:
    //  链栈的函数成员
    LinkStack();                                                  // 无参数的构造函数
    virtual ~LinkStack();                                         // 析构函数
    int GetLength() const;                                        // 求栈的长度
    bool IsEmpty() const;                                         // 判断栈是否为空
    void Clear();                                                 // 将栈清空
    void Traverse(void (*Visit)(const ElemType &)) const;         // 遍历栈
    Status Push(const ElemType &e);                               // 入栈
    Status Pop(ElemType &e);                                      // 出栈
    Status GetTop(ElemType &e) const;                             // 取栈顶元素
    LinkStack(const LinkStack<ElemType> &s);                      // 拷贝构造函数
    LinkStack<ElemType> &operator=(const LinkStack<ElemType> &s); // 重载赋值运算符
};

// 链栈类实现部分

template <class ElemType>
LinkStack<ElemType>::LinkStack()
// 操作结果：构造一个空栈
{
    head = new Node<ElemType>; // 创建头结点
    assert(head);              // 创建头结点失败，终止程序运行
    length = 0;                // 初始化栈的元素个数为0
}

template <class ElemType>
LinkStack<ElemType>::~LinkStack()
// 操作结果：销毁栈
{
    Clear();     // 清空栈
    delete head; // 释放头结点所指空间
}

template <class ElemType>
int LinkStack<ElemType>::GetLength() const
// 操作结果：返回栈的长度
{
    return length;
}

template <class ElemType>
bool LinkStack<ElemType>::IsEmpty() const
// 操作结果：如栈为空，则返回true，否则返回false
{
    return head->next == NULL;
}

template <class ElemType>
void LinkStack<ElemType>::Clear()
// 操作结果：清空栈，删除栈中所有元素结点
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

template <class ElemType>
void LinkStack<ElemType>::Traverse(void (*Visit)(const ElemType &)) const
// 操作结果：从栈底到栈顶依次对栈的每个元素调用函数(*visit)
{
    Node<ElemType> *p = head->next;
    while (p != NULL)
    {
        (*Visit)(p->data); // 对p指向的元素调用visit
        p = p->next;
    }
}

template <class ElemType>
Status LinkStack<ElemType>::Push(const ElemType &e)
// 操作结果：将元素e压入栈顶，返回SUCCESS
{
    Node<ElemType> *p;
    p = new Node<ElemType>(e, head->next); // 生成新结点
    assert(p);                             // 申请结点失败，终止程序运行
    head->next = p;                        // 将新结点插入头结点之后
    length++;                              // 栈长度加1
    return SUCCESS;
}

template <class ElemType>
Status LinkStack<ElemType>::Pop(ElemType &e)
// 操作结果：如果栈不空，那么删除栈顶元素，用e返回其值，返回SUCCESS，
//	否则返回UNDER_FLOW
{
    if (!IsEmpty())
    {                                   // 栈非空
        Node<ElemType> *p = head->next; // p指向栈顶结点
        e = p->data;                    // 用e返回栈顶元素
        head->next = p->next;           // 修改头结点指针
        delete p;                       // 释放栈顶结点
        length--;                       // 栈长度减1
        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}

template <class ElemType>
Status LinkStack<ElemType>::GetTop(ElemType &e) const
// 操作结果：如果栈不空，那么用e返回栈顶元素，返回SUCCESS，
//	否则返回UNDER_FLOW
{
    if (!IsEmpty())
    {                                   // 栈非空
        Node<ElemType> *p = head->next; // p指向栈顶结点
        e = p->data;                    // 用e返回栈顶元素
        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}

template <class ElemType>
LinkStack<ElemType>::LinkStack(const LinkStack<ElemType> &s)
// 操作结果：拷贝构造，从已知栈s构造新栈
{
    head = new Node<ElemType>; // 构造头结点
    assert(head);              // 构造头结点失败，终止程序运行
    length = s.length;         // 复制栈长度

    Node<ElemType> *bottomS = s.head->next; // bottomS指向栈s的栈底

    if (bottomS == NULL)
    { // 栈s为空
        head->next = NULL;
    }
    else
    { // 栈s非空
        // 找到栈底
        while (bottomS->next != NULL)
            bottomS = bottomS->next;

        Node<ElemType> *p = head;
        // 从栈底向栈顶复制元素
        while (bottomS != s.head)
        {
            p->next = new Node<ElemType>(bottomS->data, NULL);
            assert(p->next); // 构造元素结点失败，终止程序运行
            p = p->next;
            // 寻找bottomS的前驱
            Node<ElemType> *q = s.head->next;
            while (q->next != bottomS)
                q = q->next;
            bottomS = q;
        }
    }
}

template <class ElemType>
LinkStack<ElemType> &LinkStack<ElemType>::operator=(const LinkStack<ElemType> &s)
// 操作结果：赋值运算符重载，将栈s赋值给当前栈
{
    if (&s != this)
    {
        Clear();           // 清空当前栈
        length = s.length; // 复制栈长度

        Node<ElemType> *bottomS = s.head->next; // bottomS指向栈s的栈底

        if (bottomS == NULL)
        { // 栈s为空
            head->next = NULL;
        }
        else
        { // 栈s非空
            // 找到栈底
            while (bottomS->next != NULL)
                bottomS = bottomS->next;

            Node<ElemType> *p = head;
            // 从栈底向栈顶复制元素
            while (bottomS != s.head)
            {
                p->next = new Node<ElemType>(bottomS->data, NULL);
                assert(p->next); // 构造元素结点失败，终止程序运行
                p = p->next;
                // 寻找bottomS的前驱
                Node<ElemType> *q = s.head->next;
                while (q->next != bottomS)
                    q = q->next;
                bottomS = q;
            }
        }
    }
    return *this;
}

#endif
