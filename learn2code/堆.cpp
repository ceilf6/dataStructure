// 本文件只是生成堆的下沉算法
// ，但是这版算法复杂度比learn2code/树/二叉树/堆/最小堆.cpp的向下调整算法高一些
// （但其实都是 O(n) ）
// 因为交换次数更多了，最好是通过 temp 优化
// 更详细的请看 learn2code/树/二叉树/堆

#include <stdio.h>

void siftDown(int a[], int n, int i)
{
    while (1) // 一路向下修复
    {
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        int smallest = i;
        if (l < n && a[l] < a[smallest])
            smallest = l;
        if (r < n && a[r] < a[smallest])
            smallest = r;
        if (smallest == i)
            break; // 本来就比左右孩子小

        // 交换
        int tmp = a[i];
        a[i] = a[smallest];
        a[smallest] = tmp;

        i = smallest; // 交换后继续下沉
    }
}

void buildMinHeap(int a[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
    {
        siftDown(a, n, i);
    }
}

int main()
{
    int tar[] = {26, 78, 34, 28, 25, 66, 80, 6, 17};
    int n = 9;

    buildMinHeap(tar, n);

    for (int i = 0; i < n; i++)
        printf("%d ", tar[i]);
    return 0;
}