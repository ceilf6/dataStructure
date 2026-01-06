template <class ElemType>
class SeqStack
{
protected:
    int top; // 栈顶
    /*
    s->top == -1 表示栈空
    s->top == maxSize - 1 表示栈满
    */
    int maxSize;     // 栈最大容量
    ElemType *elems; // 元素存储

public:
    enum Status
    {
        SUCCESS,
        FAILED
        // ...
    };

    SeqStack(int size = DEFAULT_SIZE);
    virtual ~SeqStack();
    int GetLength() const;
    bool IsEmpty() const;
    void Clear();
    Status Push(const ElemType e);
    Status Top(ElemType &e) const;
    Status Pop(ElemType &e);
    void Traverse(void (*Visit)(const ElemType &)) const;
};
