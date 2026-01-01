#ifndef __GEN_LIST_CIRCULAR_H__
#define __GEN_LIST_CIRCULAR_H__

#include "Assistance.h"       // 辅助软件包
#include "GenNode_Circular.h" // 广义表结点类

// 广义表类(循环链表版本)
template <class ElemType>
class GenList
{
protected:
    // 广义表的数据成员:
    GenListNode<ElemType> *head; // 广义表头指针

    // 辅助函数:
    void ShowHelp(GenListNode<ElemType> *hd) const;
    // 显示以hd为头结点的广义表
    int DepthHelp(const GenListNode<ElemType> *hd);
    // 返回以hd为头结点的广义表深度
    void ClearHelp(GenListNode<ElemType> *hd);
    // 释放以hd为头结点的广义表结构
    void CopyHelp(const GenListNode<ElemType> *sourceHead,
                  GenListNode<ElemType> *&destHead);
    // 将destHead为头结点的广义表复制成以sourceHead为头结点的
    // 广义表
    static void CreateHelp(GenListNode<ElemType> *&first, GenListNode<ElemType> *head);
    // 创建以first为首元结点的广义表
    int CountAtomsHelp(const GenListNode<ElemType> *hd) const;
    // 辅助函数: 统计以hd为头结点的广义表中原子结点数目

public:
    // 广义表方法声明及重载编译系统默认方法声明:
    GenList();                            // 无参数的构造函数
    GenList(GenListNode<ElemType> *hd);   // 由头结点指针构造广义表
    ~GenList();                           // 析构函数
    GenListNode<ElemType> *First() const; // 返回广义表的第一个元素
    GenListNode<ElemType> *Next(GenListNode<ElemType> *p) const;
    // 返回p指向的广义表元素的后继
    bool IsEmpty() const;           // 判断广义表是否为空
    void Insert(const ElemType &e); // 将原子元素e作为表头插入到广义表当前位置
    void Insert(GenList<ElemType> &subList);
    // 将子表subList作为表头插入到广义表当前位置
    Status Delete(int i);                                     // 删除广义表中第i个元素
    int GetDepth();                                           // 求广义表深度
    int GetLength();                                          // 求广义表长度
    int CountAtoms() const;                                   // 统计广义表中原子数目
    GenList(const GenList<ElemType> &g);                      // 拷贝构造函数
    GenList<ElemType> &operator=(const GenList<ElemType> &g); // 赋值运算符
    void Input(void);                                         // 输入广义表
    void Show(void);                                          // 显示广义表
};

// 广义表类实现部分
template <class ElemType>
GenList<ElemType>::GenList()
// 操作结果: 构造一个空广义表(循环链表形式)
{
    head = new GenListNode<ElemType>(HEAD);
    head->ref = 1;      // 引用数
    head->tLink = head; // 循环链表: 指向自身
}

template <class ElemType>
GenList<ElemType>::GenList(GenListNode<ElemType> *hd)
// 操作结果: 由头结点指针构造广义表
{
    head = hd; // 头结点
}

template <class ElemType>
GenListNode<ElemType> *GenList<ElemType>::First() const
// 操作结果: 返回广义表的第一个元素
{
    if (head->tLink == head)
        return NULL; // 空表
    return head->tLink;
}

template <class ElemType>
GenListNode<ElemType> *GenList<ElemType>::Next(GenListNode<ElemType> *p) const
// 操作结果: 返回p指向的广义表元素的后继
{
    if (p->tLink == head)
        return NULL; // 已到表尾
    return p->tLink;
}

template <class ElemType>
bool GenList<ElemType>::IsEmpty() const
// 操作结果: 如广义表为空,则返回true,否则返回false
{
    return head->tLink == head; // 循环链表判空
}

template <class ElemType>
void GenList<ElemType>::Insert(const ElemType &e)
// 操作结果: 将原子元素e作为表头插入到广义表当前位置
{
    GenListNode<ElemType> *p = new GenListNode<ElemType>(ATOM, head->tLink);
    p->atom = e;     // 数据域
    head->tLink = p; // 将p插入在head和head->tLink之间
}

template <class ElemType>
void GenList<ElemType>::Insert(GenList<ElemType> &subList)
// 操作结果: 将子表subList作为表头插入到广义表当前位置
{
    GenListNode<ElemType> *p = new GenListNode<ElemType>(LIST, head->tLink);
    p->hLink = subList.head; // 子表
    subList.head->ref++;     // subList的引用数加1
    head->tLink = p;         // 将p插入在head和head->tLink之间
}

template <class ElemType>
Status GenList<ElemType>::Delete(int i)
// 操作结果: 删除广义表中第i个元素
{
    if (i < 1 || i > GetLength())
        return RANGE_ERROR; // 索引位置错
    else
    {
        GenListNode<ElemType> *pre = head, *p = head->tLink;
        for (int k = 1; k < i; k++)
        { //  使p与pre分别指向被删结点及其前驱结点
            pre = p;
            p = p->tLink;
        }
        pre->tLink = p->tLink;
        if (p->tag == LIST)
            ClearHelp(p->hLink);
        delete p;
        return SUCCESS; // 标志删除成功
    }
}

template <class ElemType>
void GenList<ElemType>::ShowHelp(GenListNode<ElemType> *hd) const
// 操作结果: 显示以hd为头结点的广义表
{
    bool first = true;
    cout << "("; // 广义表以(开始
    for (GenListNode<ElemType> *p = hd->tLink; p != hd; p = p->tLink)
    { // 依次处理广义表各元素 (循环链表遍历)
        if (first)
            first = false; // 第一个元素
        else
            cout << ",";    // 不同元素这间用逗号隔开
        if (p->tag == ATOM) // 原子结点
            cout << p->atom;
        else // 子表
            ShowHelp(p->hLink);
    }
    cout << ")"; // 广义表以)结束
}

template <class ElemType>
void GenList<ElemType>::Show(void)
// 操作结果: 显示广义表
{
    ShowHelp(head); // 调用辅助函数显示广义表
}

template <class ElemType>
int GenList<ElemType>::DepthHelp(const GenListNode<ElemType> *hd)
// 操作结果: 返回以hd为头结点的广义表深度
{
    if (hd->tLink == hd)
        return 1; // 空广义表深度为1

    int subMaxDepth = 0; // 子表最大深度
    for (GenListNode<ElemType> *p = hd->tLink; p != hd; p = p->tLink)
    { // 求子表最大深度 (循环链表遍历)
        if (p->tag == LIST)
        {                                          // 子表
            int curSubDepth = DepthHelp(p->hLink); // 子表深度
            if (subMaxDepth < curSubDepth)
                subMaxDepth = curSubDepth;
        }
    }
    return subMaxDepth + 1; // 广义表深度为子表最大深度加1
}

template <class ElemType>
int GenList<ElemType>::GetDepth()
// 操作结果: 返回广义表深度
{
    return DepthHelp(head);
}

template <class ElemType>
int GenList<ElemType>::GetLength()
// 操作结果: 返回广义表长度
{
    GenListNode<ElemType> *p = head->tLink; // 临时指针
    int length = 0;
    while (p != head)
    { // 循环链表遍历
        p = p->tLink;
        length++;
    }
    return length;
}

template <class ElemType>
int GenList<ElemType>::CountAtomsHelp(const GenListNode<ElemType> *hd) const
// 操作结果: 统计以hd为头结点的广义表中原子结点数目
{
    int count = 0;
    for (GenListNode<ElemType> *p = hd->tLink; p != hd; p = p->tLink)
    { // 循环链表遍历所有元素
        if (p->tag == ATOM)
        { // 原子结点
            count++;
        }
        else if (p->tag == LIST)
        { // 子表结点,递归统计子表中的原子数
            count += CountAtomsHelp(p->hLink);
        }
    }
    return count;
}

template <class ElemType>
int GenList<ElemType>::CountAtoms() const
// 操作结果: 统计广义表中原子结点数目
{
    return CountAtomsHelp(head);
}

template <class ElemType>
void GenList<ElemType>::ClearHelp(GenListNode<ElemType> *hd)
// 操作结果: 释放以hd为头结点的广义表结构
{
    hd->ref--; // 引用数减1

    if (hd->ref == 0)
    {                                        // 引用数为0,释放结点所占用空间
        GenListNode<ElemType> *pre = hd, *p; // 临时指针
        for (p = hd->tLink; p != hd; p = p->tLink)
        {               // 扫描广义表hd的各结点 (循环链表遍历)
            delete pre; // 释放pre
            pre = p;
            if (p->tag == LIST)      // p为子表
                ClearHelp(p->hLink); // 释放子表
        }
        delete pre; // 释放尾结点pre(即头结点)
    }
}

template <class ElemType>
GenList<ElemType>::~GenList()
// 操作结果: 释放广义表结构,析构函数
{
    ClearHelp(head);
}

template <class ElemType>
void GenList<ElemType>::CopyHelp(const GenListNode<ElemType> *sourceHead,
                                 GenListNode<ElemType> *&destHead)
// 初始条件: 以sourceHead为头结点的广义表为非递归广义表
// 操作结果: 将以sourceHead为头结点的广义表复制成以destHead为头结点的广义表
{
    destHead = new GenListNode<ElemType>(HEAD); // 生成头结点
    GenListNode<ElemType> *destPtr = destHead;  // destHead的当前结点
    destHead->ref = 1;                          // 引用数为1
    for (GenListNode<ElemType> *p = sourceHead->tLink; p != sourceHead;
         p = p->tLink)
    { // 扫描广义表sourceHead的各结点 (循环链表遍历)
        destPtr = destPtr->tLink = new GenListNode<ElemType>(p->tag);
        // 生成新结点
        if (p->tag == LIST)
        {                                       // 子表
            CopyHelp(p->hLink, destPtr->hLink); // 复制子表
        }
        else
        {                            // 原子结点
            destPtr->atom = p->atom; // 复制原子结点
        }
    }
    destPtr->tLink = destHead; // 形成循环链表
}

template <class ElemType>
GenList<ElemType>::GenList(const GenList<ElemType> &g)
// 操作结果: 由广义表g构造新广义表--拷贝构造函数
{
    CopyHelp(g.head, head);
}

template <class ElemType>
GenList<ElemType> &GenList<ElemType>::operator=(const GenList<ElemType> &g)
// 操作结果: 将广义表g赋值给当前广义表--赋值运算符
{
    if (&g != this)
    {
        ClearHelp(head);        // 清空当前广义表
        CopyHelp(g.head, head); // 复制广义表
    }
    return *this;
}

template <class ElemType>
void GenList<ElemType>::CreateHelp(GenListNode<ElemType> *&first, GenListNode<ElemType> *head)
// 操作结果: 创建以first为首元结点的广义表
{
    char ch = GetChar(); // 读入字符
    switch (ch)
    {
    case ')':         // 广义表建立结束
        first = head; // 循环链表: 指回头结点
        return;
    case '(': // 子表
        // 表头为子表
        first = new GenListNode<ElemType>(LIST); // 生成表结点

        GenListNode<ElemType> *subHead;            // 子表指针
        subHead = new GenListNode<ElemType>(HEAD); // 生成子表的头结点
        subHead->ref = 1;                          // 引用数为1
        first->hLink = subHead;                    // subHead为子表
        CreateHelp(subHead->tLink, subHead);       // 递归建立子表

        ch = GetChar(); // 读入','
        if (ch != ',')
            cin.putback(ch);            // 如不是','则将ch放回输入流中
        CreateHelp(first->tLink, head); // 创建广义表下一结点
        break;
    default: // 原子
        // 表头为原子
        cin.putback(ch);                         // 将ch放回输入流中
        ElemType amData;                         // 原子结点数据域
        cin >> amData;                           // 读入原子结点数据域
        first = new GenListNode<ElemType>(ATOM); // 生成原子结点
        first->atom = amData;                    // 原子结点数据域

        ch = GetChar(); // 读入','
        if (ch != ',')
            cin.putback(ch);            // 如不是','则将ch放回输入流中
        CreateHelp(first->tLink, head); // 创建广义表下一结点
        break;
    }
}

template <class ElemType>
void GenList<ElemType>::Input(void)
// 操作结果: 输入广义表
{
    ClearHelp(head);
    head = new GenListNode<ElemType>(HEAD); // 生成广义表头结点
    head->ref = 1;                          // 引用数为1

    GetChar(); // 读入第一个'('
    GenList<ElemType>::CreateHelp(head->tLink, head);
    // 创建以head->tLink为首元结点的广义表
}

#endif
