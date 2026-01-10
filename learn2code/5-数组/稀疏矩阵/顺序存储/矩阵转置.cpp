#include "三元组顺序表-数组压缩.h"

// 矩阵转置：像普通二维数组直接 O(1) 随机访问干就完了
// 但是三元组顺序表转置不能简单交换，会破坏行优先顺序，所以得预计算实现转置: 统计原矩阵中每一列的非零元个数
template <class ElemType>
void TriSparseMatrix<ElemType>::
    FastTranspose(const TriSparseMatrix<ElemType> &source, TriSparseMatrix<ElemType> &dest)
{
    b.rows = cols;
    b.cols = rows;
    b.num = num;
    b.maxSize = maxSize;
    delete[] b.triElems;
    b.triElems = new Triple<ElemType>[b.maxSize];
    int *cNum = new int[cols + 1]; // 存放原矩阵中每一列的非零元个数
    int *cPos = new int[cols + 1];
    int col, i;
    if (b.num > 0)
    {
        for (col = 0; col < cols; col++)
            cNum[col] = 0; // 初始化cNum
        for (i = 0; i < a.num; i++)
            ++cNum[triElems[i].col]; // 统计原矩阵中每一列的非零元个数
        cPos[0] = 0;                 // 第一列的第一个非零元在b存储的起始位置
        for (col = 1; col < cols; col++)
            cPos[col] = cPos[col - 1] + cNum[col - 1];
        for (i = 0; i < num; i++)
        { // 循环遍历原矩阵中的三元组
            int j = cPos[triElems[i].col];
            b.triElems[j].row = triElems[i].col;
            b.triElems[j].col = triElems[i].row;
            b.triElems[j].value = triElems[i].value;
            ++cPos[triElems[i].col];
        }
    }
    delete[] cNum;
    delete[] cPos;
}
