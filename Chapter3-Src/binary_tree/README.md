# 二叉树（二叉链表存储）实验 README（按 `rule.md` 规范）

上机内容  
姓    名：王景宏　　序/学号：23123994  
开发环境版本：Apple clang 14.0.3（arm64-apple-darwin24.2.0）　　日    期：2025.12.25  
头文件个数：3　　源程序文件个数：1　　工程文件名：`Chapter3-Src/binary_tree`  

---

## 1. 实现原理（可辅以流程图/伪代码等）

本实验实现了**二叉树的二叉链表存储结构**。每个结点包含：

- 数据域 `data`
- 左孩子指针 `leftChild`
- 右孩子指针 `rightChild`

二叉树本体以 `root` 指向根结点，通过递归完成遍历、求高、计数、复制与销毁。

### 1.1 递归遍历伪代码

前序（根-左-右）：

```text
PreOrder(r):
  if r != null:
    Visit(r.data)
    PreOrder(r.left)
    PreOrder(r.right)
```

中序（左-根-右）：

```text
InOrder(r):
  if r != null:
    InOrder(r.left)
    Visit(r.data)
    InOrder(r.right)
```

后序（左-右-根）：

```text
PostOrder(r):
  if r != null:
    PostOrder(r.left)
    PostOrder(r.right)
    Visit(r.data)
```

### 1.2 树高与结点数递归思想

- 树高（高度）：
  - 空树为 0
  - 非空树为 `max(左子树高, 右子树高) + 1`
- 结点数：
  - 空树为 0
  - 非空树为 `左子树结点数 + 右子树结点数 + 1`

### 1.3 销毁与拷贝

- **销毁**：后序递归，先释放左右子树再释放根结点，避免悬挂引用。
- **深拷贝**：递归复制每个结点，并分别复制左右子树，保证新旧树互不共享结点内存。

---

## 2. 实现技术（如何使用/改进完善教材程序）

### 2.1 改造来源说明

该二叉树实现注明“由双向链表改造而来”：

- `DblNode::prior` → `BinTreeNode::leftChild`
- `DblNode::next` → `BinTreeNode::rightChild`
- `DblLinkList::head` → `BinaryTree::root`
- `DblLinkList::length` → `BinaryTree::nodeCount`

### 2.2 模板与函数指针回调

- `BinaryTree` 与 `BinTreeNode` 均为**模板**，可支持 `char`、`int` 等多种数据类型。
- 遍历采用 `void (*Visit)(const ElemType&)` 回调方式，测试中直接复用 `Assistance.h` 的 `Write` 输出函数。

### 2.3 需要注意/可改进点（分析结论）

- **`InsertLeftChild/InsertRightChild` 会直接覆盖指针**：若结点原本已有孩子且被覆盖，旧子树不会被释放，可能造成内存泄漏。本实验测试用例均在空孩子处插入，因此未触发问题。
- **`nodeCount` 与 `GetNodeCount()` 的策略不一致**：插入时 `nodeCount++`，但 `GetNodeCount()` 实际走递归统计（`NodeCountHelp`）。若发生覆盖/删除等操作，`nodeCount` 可能失真；建议二选一统一策略。
- **`CreateBinTree` 在头文件中仅声明，未给出定义**：当前测试程序未调用该接口，因此编译运行正常；若外部实例化并调用，需要补齐实现（例如按先序输入+空标记建树）。

---

## 3. 文件结构说明

| 文件名 | 文件类型 | 功能简介 | 备注 |
|---|---|---|---|
| `Assistance.h` | 头文件 | 辅助工具：标准库汇总、`Status` 枚举、`Write` 输出函数 | 多章节通用 |
| `BinTreeNode.h` | 头文件 | 二叉树结点模板 `BinTreeNode`：数据域+左右孩子指针+构造函数 | 二叉链表结点 |
| `BinaryTree.h` | 头文件 | 二叉树模板 `BinaryTree`：遍历/求高/计数/插入/深拷贝/销毁等 | 主要实现 |
| `TestBinaryTree.cpp` | 源文件 | 构造两棵示例树并测试遍历、性质、拷贝与赋值 | 主程序入口 |

（目录中还可能存在已编译的可执行文件/输出文件，如 `TestBinaryTree`、`run_output.txt`，不计入源代码文件统计。）

---

## 4. 运行实测试数据和输出结果

### 4.1 编译与运行

在 `Chapter3-Src/binary_tree` 目录下：

```bash
g++ -std=c++17 -O2 -Wall -Wextra -pedantic TestBinaryTree.cpp -o TestBinaryTree.out
./TestBinaryTree.out
```

（macOS 上也可用 `clang++` 编译。）

### 4.2 代表性测试 1：字符二叉树（A~I）

测试数据：程序中手动插入，结构为：

```text
            A
           / \
          B   C
         / \   \
        D   E   F
           /   / \
          G   H   I
```

关键输出（与 `run_output.txt` 一致）：

```text
1. 前序遍历（根-左-右）：A B D E G C F H I 
2. 中序遍历（左-根-右）：D B G E A C H F I 
3. 后序遍历（左-右-根）：D G E B H I F C A 

树的深度（高度）：4
结点总数：9
叶子结点个数：4
单分支结点个数：2
双分支结点个数：3
验证结果：正确 ✓（n0 = n2 + 1）
```

### 4.3 代表性测试 2：整数完全二叉树（1~5）

测试数据：程序中手动插入，结构为：

```text
            1
           / \
          2   3
         / \
        4   5
```

关键输出：

```text
前序遍历：1 2 4 5 3 
中序遍历：4 2 5 1 3 
后序遍历：4 5 2 3 1 
树的深度：3
结点总数：5
叶子结点数：3
```

---

## 5. 个人体会

- 通过把“双向链表结点”改造成“二叉树结点”，能直观体会**指针域语义变化**：链表的前驱/后继在树里变成了左/右孩子。
- 递归在二叉树中非常自然：遍历、求高、计数、销毁、复制都能用同一类“分治”思想表达，代码结构清晰。
- 调试时最需要注意的是**空指针分支**与**内存释放顺序**（后序销毁最安全）。
- 进一步完善时，建议统一结点计数策略，并为 `CreateBinTree` 补齐输入建树实现，同时在插入时处理“原孩子不为空”的情况以避免内存泄漏。

---

## 6. 参考资料（GB/T 7714-2015 形式）

[1] 严蔚敏, 吴伟民. 数据结构（C语言版）[M]. 北京: 清华大学出版社, 2007.  
[2] cppreference.com. *assert* — C++ Reference[EB/OL]. (2025-12-25)[2025-12-25]. `https://en.cppreference.com/w/cpp/error/assert`  


