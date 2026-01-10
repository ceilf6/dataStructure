#include "十字链表.h"

template <class ElemType>
Status CrossList<ElemType>::SetElem(int r, int c, const ElemType &v)
{
    if (r >= rows || c >= cols || r < 0 || c < 0)
        return RANGE_ERROR;
    CrossNode<ElemType> *pre, *p;
    if (v == 0)
    {
        pre = NULL;
        p = rowHead[r];
        while (p != NULL && p->triElem.col < c)
        {
            pre = p;
            p = p->right;
        }
        if (p != NULL && p->triElem.col == c)
        {
            if (rowHead[r] == p)
                rowHead[r] = p->right;
            else
                pre->right = p->right;
            if (colHead[c] == p)
                colHead[c] = p->down;
            else
            {
                pre = colHead[c];
                while (pre->down != p)
                    pre = pre->down;
                pre->down = p->down;
            }
            delete p;
            num--;
        }
    }
    else
    { // 把第r行、第c列的元素值修改为非零元素
        pre = NULL;
        p = rowHead[r];
        while (p != NULL && p->triElem.col < c)
        {
            pre = p;
            p = p->right;
        }

        if (p != NULL && p->triElem.col == c)
            p->triElem.value == v;
        else
        { // 原结点为0元素，则需要插入结点
            Triple<ElemType> e(r, c, v);
            CrossNode<ElemType> *ePtr = new CrossNode<ElemType>(e);
            if (rowHead[r] == p)
                rowHead[r] = ePtr;
            else
                pre->right = ePtr;
            ePtr->right = p;
            pre = NULL;
            p = colHead[c];
            while (p != NULL && p->triElem.row < r)
            {
                pre = p;
                p = p->down;
            }
            if (colHead[c] == p)
                colHead[c] = ePtr;
            else
                pre->down = ePtr;
            ePtr->down = p;
            num++;
        }
    }
    return SUCCESS;
}

template <class ElemType>
Status CrossList<ElemType>::GetElem(int r, int c, ElemType &v)
{
    if (r >= rows || c >= cols || r < 0 || c < 0)
        return RANGE_ERROR;
    CrossNode<ElemType> *p;
    for (p = rowHead[r]; p != NULL && p->triElem.col < c; p = p->right)
        ;
    if (p != NULL && p->triElem.col == c) // 找到三元组
        v = p->triElem.value;
    else // 未找到三元组
        v = 0;
    return SUCCESS;
}

template <class ElemType>
CrossList<ElemType> CrossList<ElemType>::operator+(const CrossList<ElemType> &b)
{
    if (rows != b.rows || cols != b.cols)
        throw Error("行数或列数不相等!");
    CrossList<ElemType> temp(b.rows, b.cols);
    ElemType v;
    CrossNode<ElemType> *p, *q;
    for (int i = 0; i < rows; i++)
    {
        p = rowHead[i];
        q = b.rowHead[i];
        while (p != NULL && q != NULL)
            if (p->triElem.col < q->triElem.col)
            {
                temp.SetElem(p->triElem.row, p->triElem.col, p->triElem.value);
                p = p->right;
            }
            else if (p->triElem.col > q->triElem.col)
            {
                temp.SetElem(q->triElem.row, q->triElem.col,
                             q->triElem.value);
                q = q->right;
            }
            else
            {
                v = p->triElem.value + q->triElem.value;
                if (v != 0)
                    temp.SetElem(q->triElem.row, q->triElem.col, v);
                p = p->right;
                q = q->right;
            }
        while (p != NULL)
        {
            temp.SetElem(p->triElem.row, p->triElem.col, p->triElem.value);
            p = p->right;
        }
        while (q != NULL)
        {
            temp.SetElem(q->triElem.row, q->triElem.col, q->triElem.value);
            q = q->right;
        }
    }
    return temp;
}
