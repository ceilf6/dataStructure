template <class ElemType>
struct Node // 节点类
{
    ElemType data;
    Node<ElemType> *next;

    Node();
    Node(ElemType e, Node<ElemType> *link = NULL);
};
// 节点的构造函数
template <class ElemType>
Node<ElemType>::Node()
{
    next = NULL;
}
template <class ElemType>
Node<ElemType>::Node(ElemType e, Node<ElemType> *link)
{
    data = e;
    next = link;
}
