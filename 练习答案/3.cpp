using namespace std;

template <class ElemType>
Status SeqList<ElemType>::DeleteMinElem(ElemType &e)
{
    if (length == 0)
        return UNDER_FLOW;
    else
    {
        int idx = 0;
        for (int i; i < length; i++)
            if (elems[i] < elems[idx])
                idx = i;
        e = elems[idx];
        length--; // 注意length是最后一个元素的下一个位置，所以得先减
        elems[idx] = elems[length];
        return SUCCESS;
    }
}

// 1.2
status seq::deleteV(const ElemType v)
{
    int k = 0;
    ElemType temp;

    for (int i = 0; i < length; i++)
    {
        GetElem(i, temp);
        if (temp != v)
        {
            SetElem(k, temp);
            k++;
        }
    }

    length = k;
    return OK;
}
// 参考答案是直接调用的 GetElem 和 DeleteElem

// 9
/*
int count = 1;
p->freq++;
其中 count 是在数组中出现的逻辑下标
freq才是统计的出现频率
*/
template <class ElemType>
struct DblNode
{
    ElemType data;
    int freq;
    DblNode *prior;
    DblNode *next;
};

template <class ElemType>
class DblLinkList
{
public:
    DblNode<ElemType> *head; // 带头结点
    int LocateElem(const ElemType &e);
};

template <class ElemType>
int DblLinkList<ElemType>::LocateElem(const ElemType &e)
{
    DblNode<ElemType> *p = head->next; // 1) 从首元结点开始找
    int pos = 1;                       // 2) 记录 p 当前的逻辑位置（从1开始）

    // 3) 顺序查找值为 e 的结点
    while (p != NULL && p->data != e)
    {
        p = p->next;
        pos++;
    }

    // 4) 没找到，返回 0（也可以按教材返回 -1）
    if (p == NULL)
        return 0;

    // 5) 找到了：访问频度 +1
    p->freq++;

    // 6) 从 p 的前驱开始，向前找应该插入的位置 q
    //    目标：找到“最后一个 freq >= p->freq 的结点”作为 q（q 可能是 head）
    DblNode<ElemType> *q = p->prior;
    while (q != head && q->freq < p->freq)
    {
        q = q->prior; // 7) q 向前走，表示 p 将跨过一个结点
        pos--;        // 8) p 每跨过一个结点，最终位置就前移一位，所以 pos--
    }

    // 9) 如果 q 仍然是 p 的前驱，说明 p 不需要移动，直接返回位置
    if (q == p->prior)
        return pos;

    // 10) 否则：把 p 从原位置“摘下来”（断链）
    DblNode<ElemType> *a = p->prior;
    DblNode<ElemType> *b = p->next;
    a->next = b;
    if (b != NULL)
        b->prior = a;

    // 11) 把 p 插入到 q 之后（即 q 与 q->next 之间）
    p->prior = q;
    p->next = q->next;
    if (q->next != NULL)
        q->next->prior = p;
    q->next = p;

    // 12) 返回调整后的逻辑位置
    return pos;
}