1. 顺序数组实现的节点在删除时不需要delete但是链式的需要
    
    因为 数组实现是直接创造了一大片空间，元素并不需要 new 空间而是直接存入
    
    而链式的话每个节点都需要 **new** Node ，所以在删除时需要 delete
    
2. 顺序结构需要容量加位置（指针），链式结构只需要入口指针
顺序实现一般都是
    
    ```cpp
    class {
    protected:
    	int 管理指针;
    	int maxSize;
    	ElemType *elems; // 元素存储
    }
    ```
    
    链式一般就是个头
    
    ```cpp
    class {
    protected:
    	Node* head;	
    }
    ```