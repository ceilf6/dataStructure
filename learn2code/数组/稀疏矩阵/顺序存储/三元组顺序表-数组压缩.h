/*
  原矩阵:              三元组表:
  0 0 3 0              row  col  value
  0 0 0 0      →       0    2    3
  4 0 0 5              2    0    4
                       2    3    5
  用数组存储所有 Triple，按行优先排序。
  牺牲了数组 O(1) 的随机访问能力换取降低空间复杂度
  - "稀疏矩阵压缩后必回失去随机存取能力"
    - 普通数组：地址 = base + i*cols + j 这是 O(1) 的
      一般矩阵在压缩后位置不再由行列决定，需要去查找
    - 但是哈希表的存储是用 (row, col) 作为 key
        unordered_map<pair<int,int>, ElemType> sparse;

        // 访问 A[i][j]
        sparse[{i, j}]  // 平均 O(1)
      所以错误
*/

template <class ElemType>
class TriSparseMatrix
{
protected:
    // 稀疏矩阵三元组顺序表的数据成员:
    Triple<ElemType> *triElems;
    int maxSize;
    int rows, cols, num;

public:
    TriSparseMatrix(int rs = DEFAULT_SIZE, int cs = DEFAULT_SIZE, int size = DEFAULT_SIZE);
    ~TriSparseMatrix();  // 析构函数
    int GetRows() const; // 返回稀疏矩阵行数
    int GetCols() const; // 返回稀疏矩阵列数
    int GetNum() const;  // 返回稀疏矩阵非零元个数
    Status SetElem(int r, int c, const ElemType &v);
    Status GetElem(int r, int c, ElemType &v);
    TriSparseMatrix<ElemType> &operator=(const TriSparseMatrix<ElemType> &copy);
    // 赋值运算符重载
    void SimpleTranspose(const TriSparseMatrix<ElemType>
                             &source,
                         TriSparseMatrix<ElemType> &dest);
    // 将稀疏矩阵source转置成稀疏矩阵dest的简单算法
    void FastTranspose(const TriSparseMatrix<ElemType> &source, TriSparseMatrix<ElemType> &dest);
    // 将稀疏矩阵source转置成稀疏矩阵dest的快速算法
};
