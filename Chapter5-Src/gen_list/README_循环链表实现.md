# 广义表循环链表实现说明

## 项目概述
本项目将广义表的存储结构从普通链表改造为**带头结点的循环链表**，并实现了统计原子数目的功能。

## 文件说明

### 1. GenNode_Circular.h
广义表结点的循环链表版本定义。

**主要改进：**
- `tLink`指针：最后一个结点的tLink指向头结点，形成循环
- 支持三种结点类型：HEAD(头结点)、ATOM(原子结点)、LIST(子表结点)

### 2. GenList_Circular.h
广义表类的循环链表版本实现。

**核心改造点：**

#### (1) 构造函数
```cpp
GenList<ElemType>::GenList()
{
    head = new GenListNode<ElemType>(HEAD);
    head->ref = 1;
    head->tLink = head;  // 循环链表：指向自身
}
```

#### (2) 判空操作
```cpp
bool IsEmpty() const
{
    return head->tLink == head;  // 循环链表判空条件
}
```

#### (3) 遍历操作
所有遍历操作从 `p != NULL` 改为 `p != head`：
```cpp
for (GenListNode<ElemType> *p = hd->tLink; p != hd; p = p->tLink)
{
    // 处理结点...
}
```

#### (4) 统计原子数目 ⭐新增功能
```cpp
int CountAtomsHelp(const GenListNode<ElemType> *hd) const
{
    int count = 0;
    for (GenListNode<ElemType> *p = hd->tLink; p != hd; p = p->tLink)
    {
        if (p->tag == ATOM)
            count++;
        else if (p->tag == LIST)
            count += CountAtomsHelp(p->hLink);  // 递归统计子表
    }
    return count;
}

int CountAtoms() const
{
    return CountAtomsHelp(head);
}
```

#### (5) 创建广义表
```cpp
void CreateHelp(GenListNode<ElemType> *&first, GenListNode<ElemType> *head)
{
    // 当遇到')'时，让first指向head形成循环
    if (ch == ')') {
        first = head;  // 循环链表：指回头结点
        return;
    }
    // 其他逻辑...
}
```

### 3. AutoTest_Circular.cpp
自动化测试程序（无需交互输入）

**测试内容：**
- ✅ 空表测试
- ✅ 简单广义表测试
- ✅ 嵌套子表测试
- ✅ 复杂广义表测试
- ✅ 循环链表特性测试
- ✅ 原子计数功能测试

### 4. TestGenList_Circular.cpp
交互式测试程序（带菜单）

## 测试结果

### 测试1：空表
```
空表 = ()
长度: 0
深度: 1
原子数目: 0
```

### 测试2：简单广义表
```
广义表 g1 = (a,b,c)
长度: 3
深度: 1
原子数目: 3
```

### 测试3：嵌套子表
```
主表 = (w,(x,y),z)
长度: 3
深度: 2
原子数目: 4
```

### 测试4：复杂广义表
```
广义表 g2 = (a,(b,c,d),e,(f,(g,h)))
长度: 4
深度: 3
原子数目: 8  ✓ 正确！
```

## 循环链表的优势

1. **结构统一**：不需要特殊处理NULL指针
2. **简化判断**：判空条件统一为 `head->tLink == head`
3. **遍历高效**：结束条件明确，不需要额外判断
4. **易于扩展**：可以方便地实现双向循环链表

## 关键算法复杂度

- **统计原子数目**：O(n)，n为所有结点总数（包括子表结点）
- **求深度**：O(n)
- **求长度**：O(m)，m为第一层元素个数
- **插入/删除**：O(1)或O(k)，k为位置索引

## 编译运行

```bash
# 编译自动测试程序
cd /Users/a86198/Desktop/dataStructure/Chapter5-Src/gen_list
g++ -o AutoTest_Circular AutoTest_Circular.cpp -std=c++11

# 运行
./AutoTest_Circular

# 编译交互式程序
g++ -o TestGenList_Circular TestGenList_Circular.cpp -std=c++11

# 运行
./TestGenList_Circular
```

## 总结

本项目成功实现了：
1. ✅ 带头结点的循环链表存储结构
2. ✅ 统计原子数目的功能
3. ✅ 完整的测试验证
4. ✅ 保持了原有广义表的所有功能

所有测试用例均通过，原子计数功能准确无误！
