/*
CSC (Compressed Sparse Column) - 压缩稀疏列格式

优点：
1. 列遍历极快：O(1) 定位某列起始位置，遍历该列 O(该列非零元个数)
2. 矩阵转置简单：CSR 的转置就是 CSC，只需交换 row/col 的角色
3. 列切片高效：提取某几列形成子矩阵非常快
4. 某些算法更优：如 LU 分解、稀疏直接求解器

缺点：
1. 行访问慢：需遍历整个数组
2. 矩阵-向量乘法较慢：相比 CSR 缓存不友好
3. 插入/删除代价大：同 CSR

适用场景：
- 按列访问的算法
- 矩阵分解 (LU, Cholesky)
- 与 CSR 配合使用（同时存两份，空间换时间）

CSR vs CSC 关系：
- CSC(A) = CSR(Aᵀ)
- 矩阵 A 的 CSC 存储 = 矩阵 Aᵀ 的 CSR 存储
*/

#ifndef CSC_H
#define CSC_H

template <class ElemType>
class CSCMatrix
{
protected:
    ElemType *values; // 非零元素值数组，长度 = num
    int *rowIdx;      // 行索引数组，长度 = num
    int *colPtr;      // 列指针数组，长度 = cols + 1
    int rows, cols;   // 矩阵行数、列数
    int num;          // 非零元素个数

public:
    CSCMatrix(int rs, int cs);
    ~CSCMatrix();

    int GetRows() const { return rows; }
    int GetCols() const { return cols; }
    int GetNum() const { return num; }

    // 获取元素 A[r][c]
    ElemType GetElem(int r, int c) const;

    // 遍历第 c 列的所有非零元素，对每个元素调用 visit(row, value)
    template <class Visitor>
    void TraverseCol(int c, Visitor visit) const;

    // 向量-矩阵乘法：y = xᵀ * A（按列计算更高效）
    void SpMV_T(const ElemType *x, ElemType *y) const;

    // 从三元组数组构建 CSC（三元组需按列优先排序）
    void BuildFromTriples(int *tripleRows, int *tripleCols,
                          ElemType *tripleVals, int tripleNum);

    // 提取第 c 列作为稠密向量
    void ExtractColumn(int c, ElemType *colVec) const;
};

// ==================== 实现 ====================

template <class ElemType>
CSCMatrix<ElemType>::CSCMatrix(int rs, int cs)
    : rows(rs), cols(cs), num(0)
{
    values = nullptr;
    rowIdx = nullptr;
    colPtr = new int[cols + 1]();
}

template <class ElemType>
CSCMatrix<ElemType>::~CSCMatrix()
{
    delete[] values;
    delete[] rowIdx;
    delete[] colPtr;
}

template <class ElemType>
ElemType CSCMatrix<ElemType>::GetElem(int r, int c) const
{
    if (r < 0 || r >= rows || c < 0 || c >= cols)
        return ElemType();

    // 在第 c 列中查找行 r
    int start = colPtr[c];
    int end = colPtr[c + 1];

    for (int i = start; i < end; i++)
    {
        if (rowIdx[i] == r)
            return values[i];
        if (rowIdx[i] > r)
            break; // 行索引有序，提前退出
    }
    return ElemType();
}

template <class ElemType>
template <class Visitor>
void CSCMatrix<ElemType>::TraverseCol(int c, Visitor visit) const
{
    if (c < 0 || c >= cols)
        return;

    for (int i = colPtr[c]; i < colPtr[c + 1]; i++)
    {
        visit(rowIdx[i], values[i]);
    }
}

template <class ElemType>
void CSCMatrix<ElemType>::SpMV_T(const ElemType *x, ElemType *y) const
{
    // y = xᵀ * A，等价于 y[j] = sum(x[i] * A[i][j])
    // 按列遍历更高效

    // 初始化 y
    for (int j = 0; j < cols; j++)
        y[j] = ElemType();

    // 按列累加
    for (int j = 0; j < cols; j++)
    {
        for (int k = colPtr[j]; k < colPtr[j + 1]; k++)
        {
            y[j] += x[rowIdx[k]] * values[k];
        }
    }
}

template <class ElemType>
void CSCMatrix<ElemType>::BuildFromTriples(int *tripleRows, int *tripleCols,
                                           ElemType *tripleVals, int tripleNum)
{
    num = tripleNum;

    delete[] values;
    delete[] rowIdx;

    values = new ElemType[num];
    rowIdx = new int[num];

    // 初始化 colPtr
    for (int i = 0; i <= cols; i++)
        colPtr[i] = 0;

    // 统计每列非零元个数
    for (int i = 0; i < num; i++)
        colPtr[tripleCols[i] + 1]++;

    // 累加得到每列起始位置
    for (int i = 1; i <= cols; i++)
        colPtr[i] += colPtr[i - 1];

    // 填充 values 和 rowIdx
    // 需要临时数组记录每列当前填充位置
    int *tempPtr = new int[cols];
    for (int i = 0; i < cols; i++)
        tempPtr[i] = colPtr[i];

    for (int i = 0; i < num; i++)
    {
        int c = tripleCols[i];
        int pos = tempPtr[c]++;
        values[pos] = tripleVals[i];
        rowIdx[pos] = tripleRows[i];
    }

    delete[] tempPtr;
}

template <class ElemType>
void CSCMatrix<ElemType>::ExtractColumn(int c, ElemType *colVec) const
{
    // 初始化为零
    for (int i = 0; i < rows; i++)
        colVec[i] = ElemType();

    // 填充非零元素
    for (int k = colPtr[c]; k < colPtr[c + 1]; k++)
    {
        colVec[rowIdx[k]] = values[k];
    }
}

#endif
