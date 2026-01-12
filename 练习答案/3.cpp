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