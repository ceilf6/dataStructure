/*
用数组模拟链表

逻辑上是链表，物理上是数组

用数组定义的，存储空间大小不会变化

不允许改变各元素的物理位置，只需要重新链接就能改变顺序

## 和普通链表区别

| **普通链表** | **静态链表** |
| --- | --- |
| 用指针 | 用数组下标 |
| 动态申请内存 | 一次性申请数组 |
| next 是地址 | next 是整数 |

## 场景

- 不能使用指针
- 内存必须预先分配

数值域 + next指针域
*/

struct Node
{
    int data; // 数据域
    int next; // 游标（下一个结点的数组下标）
};

// 分配结点
int malloc_node(Node *list)
{
    int i = list[1].next; // 取第一个空闲结点
    if (i != 0)
        list[1].next = list[i].next;
    return i;
}
// 释放节点
void free_node(int i, Node *list)
{
    list[i].next = list[1].next;
    list[1].next = i;
}
// 插入节点
void insert(int x, int k, Node *list)
{
    int newNode = malloc_node(list);
    list[newNode].data = x;

    list[newNode].next = list[k].next;
    list[k].next = newNode;
}

int main()
{
    const int MAXSIZE = 100;
    Node list[MAXSIZE];

    // 初始化
    for (int i = 1; i < MAXSIZE - 1; i++)
    {
        list[i].next = i + 1;
    }
    list[MAXSIZE - 1].next = 0; // 备用链表结束

    return 0;
}

/*
## 备用链表（空闲链表）

因为静态链表大小固定所以即使删除节点，该内存空间也无法释放，所以需要用备用链表管理、再利用空间

list[1] 是备用链表头

```cpp
list[1].next → 所有空闲结点
```
*/