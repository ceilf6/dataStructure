struct Node
{
    int data; // 数据域
    int next; // 游标（下一个结点的数组下标）
};

// 通过类进行管理就不需要像main中每次要对函数传入属性
class SolidLink
{
protected:
    int maxSize;
    Node *list;

public:
    explicit SolidLink(int size);
    ~SolidLink();

    int malloc_node();
    void free_node(int i);
    void insert(int x, int k);
};