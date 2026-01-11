#include "最小堆.h"

template <class ElemType>
MinHeap<ElemType>::
    MinHeap(int maxSize)
{
    if (maxSize <= 0)
    {
        cerr << "堆的大小不能小于1" << endl;
        exit(1);
    }
    MaxSize = maxSize;
    heapArr = new ElemType[MaxSize];
    CurrentSize = 0;
}

// 向下调整算法
// 前提：除了当前节点，下面已经是堆
// 一般用在 删除堆顶/建堆
template <class ElemType>
void MinHeap<ElemType>::FilterDown(const int Start)
{
    int i = Start, child;
    ElemType temp = heapArr[i]; // 用temp可以减少交换次数，类似于插入排序的思想
    child = 2 * i + 1;          // 左孩子开始
    while (child <= CurrentSize - 1)
    {
        // 如果有右孩子，选更小的更合适当堆顶
        if (child < CurrentSize - 1 && heapArr[child + 1] < heapArr[child])
            child++;
        // 如果父节点已经是最小的，结束
        if (temp <= heapArr[child])
            break;
        else
        {
            heapArr[i] = heapArr[child]; // 孩子上提
            i = child;
            child = 2 * child + 1; // 一直向下调整下一层，因为当前操作影响的可能不止当前层
        }
    }
    heapArr[i] = temp; // 将需要向下调整的节点放到堆顶元素交换上来后的空位上
}

// 利用向下调整算法建堆：从最后一个非叶子节点开始往前对每个元素做向下调整（叶子节点已经是堆了）
// 最后一个叶子节点是 n/2-1 位置
template <class ElemType>
MinHeap<ElemType>::MinHeap(ElemType a[], int maxSize, int n)
{
    if (n <= 0)
    {
        cerr << "堆的大小不能小于1" << endl;
        exit(1);
    }
    MaxSize = maxSize;
    heapArr = new ElemType[MaxSize];
    for (int i = 0; i < n; i++)
        heapArr[i] = a[i];
    CurrentSize = n;
    int i = CurrentSize / 2 - 1; // 最后一个叶子节点位置
    while (i >= 0)
    {
        FilterDown(i);
        i--;
        Traverse(Write<ElemType>);
        cout << endl;
    }
}

// 向上调整算法
// 通常在插入新元素时使用
// 因为为保证完全二叉树性质，插入只能放在末尾。然后一路向上和父元素比较确保堆的性质
template <class ElemType>
void MinHeap<ElemType>::FilterUp(int End)
{
    int j = End, i;
    ElemType temp = heapArr[j]; // 通过 temp 保存新插入的节点，下面就是在找插入 tmp 的合适位置
    i = (j - 1) / 2;            // 父元素
    while (j > 0)
    {
        if (heapArr[i] <= temp)
            break;
        else
        {
            heapArr[j] = heapArr[i];
            j = i;           // 上提
            i = (j - 1) / 2; // 上提的父元素
        }
    }
    heapArr[j] = temp; // 在最后找到了合适的插入位置后，将 temp 放到 j 的位置。PPT中将本句放在了 while 里面这是错的
}

template <class ElemType>
Status MinHeap<ElemType>::Insert(const ElemType &e)
{
    if (IsFull())
        return OVER_FLOW;
    heapArr[CurrentSize] = e;
    FilterUp(CurrentSize);
    CurrentSize++;
    return SUCCESS;
}

// 删除堆顶
// 删除不能直接删，得用最后一个元素覆盖，否则就破坏了堆的完整性
// 然后再从删除位置开始修复
template <class ElemType>
Status MinHeap<ElemType>::DeleteTop(ElemType &e)
{
    if (IsEmpty())
        return UNDER_FLOW;
    e = heapArr[0];
    heapArr[0] = heapArr[CurrentSize - 1];
    CurrentSize--; // 最后一个元素已经上提了，直接减没问题
    FilterDown(0); // 从删除位置开始修复，也就是根节点索引 0 的位置
    return SUCCESS;
}
