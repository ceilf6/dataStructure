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

status seq::deleteV(const ElemType v)
{
    int k = 0; // k 表示新数组中应放置的位置

    for (int i = 0; i < length; i++)
    {
        if (elems[i] != v)
        {
            elems[k++] = elems[i];
        }
    }

    length = k; // 更新顺序表长度
    return OK;
}