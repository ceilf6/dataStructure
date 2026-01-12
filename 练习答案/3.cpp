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