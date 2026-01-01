#ifndef __GEN_NODE_H__
#define __GEN_NODE_H__

#ifndef __REF_GEN_LIST_NODE_TYPE__
#define __REF_GEN_LIST_NODE_TYPE__
enum GenListNodeType
{
    HEAD,
    ATOM,
    LIST
};
#endif

// 广义表结点结构(循环链表版本)
template <class ElemType>
struct GenListNode
{
    // 数据成员:
    GenListNodeType tag;
    // 标志域,HEAD(0):头结点, ATOM(1):原子结构, LIST(2):子表结构
    GenListNode<ElemType> *tLink; // 指向同一层次的下一个结点指针(循环链表,最后指回头结点)
    union
    {
        int ref;                      // tag=HEAD,头结点,引用计数域
        ElemType atom;                // tag=ATOM,存储原子结点数据域
        GenListNode<ElemType> *hLink; // tag=LIST,存储指向子表的指针域
    };

    // 构造函数:
    GenListNode(GenListNodeType tg = HEAD, GenListNode<ElemType> *next = NULL);
    // 由标志tg和指针next构造结点对象
};

// 广义表结点类实现部分
template <class ElemType>
GenListNode<ElemType>::GenListNode(GenListNodeType tg, GenListNode<ElemType> *next)
// 操作结果: 由标志tg和指针next构造结点对象
{
    tag = tg;     // 标志
    tLink = next; // 链域
}

#endif
