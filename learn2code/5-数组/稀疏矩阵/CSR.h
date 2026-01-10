/*
CSR (Compressed Sparse Row) - 压缩稀疏行格式

优点：
1. 空间效率高：只需 2*num + rows+1 的空间，比三元组的 3*num 更省
2. 行遍历极快：O(1) 定位某行起始位置，遍历该行 O(该行非零元个数)
3. 矩阵-向量乘法高效：y = A*x 按行计算，缓存友好
4. 工业标准：SciPy、MATLAB、TensorFlow 等都用 CSR

缺点：
1. 列访问慢：需遍历整个 values 数组
2. 插入/删除代价大：需移动大量元素
3. 构建后难以修改：适合"一次构建，多次使用"的场景

适用场景：
- 矩阵-向量乘法 (SpMV)
- 按行访问的算法
- 稀疏线性方程组求解
*/

#ifndef CSR_H
#define CSR_H

template <class ElemType>
class CSRMatrix
{
protected:
    ElemType *values; // 非零元素值数组，长度 = num
    int *colIdx;      // 列索引数组，长度 = num
    int *rowPtr;      // 行指针数组，长度 = rows + 1
    int rows, cols;   // 矩阵行数、列数
    int num;          // 非零元素个数

public:
    CSRMatrix(int rs, int cs);
    ~CSRMatrix();

    int GetRows() const { return rows; }
    int GetCols() const { return cols; }
    int GetNum() const { return num; }

    // 获取元素 A[r][c]
    ElemType GetElem(int r, int c) const;

    // 遍历第 r 行的所有非零元素，对每个元素调用 visit(col, value)
    template <class Visitor>
    void TraverseRow(int r, Visitor visit) const;

    // 矩阵-向量乘法：y = A * x
    void SpMV(const ElemType *x, ElemType *y) const;

    // 从三元组数组构建 CSR（三元组需按行优先排序）
    void BuildFromTriples(int *tripleRows, int *tripleCols,
                          ElemType *tripleVals, int tripleNum);
};

// ==================== 实现 ====================

template <class ElemType>
CSRMatrix<ElemType>::CSRMatrix(int rs, int cs)
    : rows(rs), cols(cs), num(0)
{
    values = nullptr;
    colIdx = nullptr;
    rowPtr = new int[rows + 1]();
}

template <class ElemType>
CSRMatrix<ElemType>::~CSRMatrix()
{
    delete[] values;
    delete[] colIdx;
    delete[] rowPtr;
}

template <class ElemType>
ElemType CSRMatrix<ElemType>::GetElem(int r, int c) const
{
    if (r < 0 || r >= rows || c < 0 || c >= cols)
        return ElemType(); // 越界返回默认值

    // 在第 r 行中二分查找列 c
    int start = rowPtr[r];
    int end = rowPtr[r + 1];

    for (int i = start; i < end; i++)
    {
        if (colIdx[i] == c)
            return values[i];
        if (colIdx[i] > c)
            break; // 列索引有序，提前退出
    }
    return ElemType(); // 零元素
}

template <class ElemType>
template <class Visitor>
void CSRMatrix<ElemType>::TraverseRow(int r, Visitor visit) const
{
    if (r < 0 || r >= rows)
        return;

    for (int i = rowPtr[r]; i < rowPtr[r + 1]; i++)
    {
        visit(colIdx[i], values[i]);
    }
}

template <class ElemType>
void CSRMatrix<ElemType>::SpMV(const ElemType *x, ElemType *y) const
{
    // y = A * x
    // y[i] = sum(A[i][j] * x[j]) for all j where A[i][j] != 0
    for (int i = 0; i < rows; i++)
    {
        ElemType sum = ElemType();
        for (int k = rowPtr[i]; k < rowPtr[i + 1]; k++)
        {
            sum += values[k] * x[colIdx[k]];
        }
        y[i] = sum;
    }
}

template <class ElemType>
void CSRMatrix<ElemType>::BuildFromTriples(int *tripleRows, int *tripleCols,
                                           ElemType *tripleVals, int tripleNum)
{
    num = tripleNum;

    delete[] values;
    delete[] colIdx;

    values = new ElemType[num];
    colIdx = new int[num];

    // 初始化 rowPtr
    for (int i = 0; i <= rows; i++)
        rowPtr[i] = 0;

    // 统计每行非零元个数
    for (int i = 0; i < num; i++)
        rowPtr[tripleRows[i] + 1]++;

    // 累加得到每行起始位置
    for (int i = 1; i <= rows; i++)
        rowPtr[i] += rowPtr[i - 1];

    // 填充 values 和 colIdx（假设三元组已按行优先排序）
    for (int i = 0; i < num; i++)
    {
        values[i] = tripleVals[i];
        colIdx[i] = tripleCols[i];
    }
}

#endif
