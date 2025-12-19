#include "BinaryTree.h"

// 计算叶子结点个数的辅助函数
template <class ElemType>
int CountLeafNodes(BinTreeNode<ElemType> *r)
{
    if (r == NULL)
        return 0;
    else if (r->leftChild == NULL && r->rightChild == NULL)
        return 1; // 叶子结点
    else
        return CountLeafNodes(r->leftChild) + CountLeafNodes(r->rightChild);
}

// 计算单分支结点个数的辅助函数
template <class ElemType>
int CountSingleChildNodes(BinTreeNode<ElemType> *r)
{
    if (r == NULL)
        return 0;
    else if ((r->leftChild != NULL && r->rightChild == NULL) ||
             (r->leftChild == NULL && r->rightChild != NULL))
        return 1 + CountSingleChildNodes(r->leftChild) + CountSingleChildNodes(r->rightChild);
    else
        return CountSingleChildNodes(r->leftChild) + CountSingleChildNodes(r->rightChild);
}

// 计算双分支结点个数的辅助函数
template <class ElemType>
int CountDoubleChildNodes(BinTreeNode<ElemType> *r)
{
    if (r == NULL)
        return 0;
    else if (r->leftChild != NULL && r->rightChild != NULL)
        return 1 + CountDoubleChildNodes(r->leftChild) + CountDoubleChildNodes(r->rightChild);
    else
        return CountDoubleChildNodes(r->leftChild) + CountDoubleChildNodes(r->rightChild);
}

// 打印分隔线
void PrintSeparator(const string &title = "")
{
    cout << "============================================" << endl;
    if (!title.empty())
        cout << "    " << title << endl;
    cout << "============================================" << endl;
}

// 打印子分隔线
void PrintSubSeparator()
{
    cout << "--------------------------------------------" << endl;
}

int main()
{
    PrintSeparator("二叉树的二叉链表存储结构演示");
    cout << endl;

    cout << "【说明】本程序由双向链表改造而来：" << endl;
    cout << "  1. 将 DblNode 的 prior 改为 BinTreeNode 的 leftChild" << endl;
    cout << "  2. 将 DblNode 的 next 改为 BinTreeNode 的 rightChild" << endl;
    cout << "  3. 将 DblLinkList 的 head 改为 BinaryTree 的 root" << endl;
    cout << "  4. 将 length 改为 nodeCount" << endl;
    cout << endl;

    PrintSubSeparator();
    cout << "构建如下二叉树结构：" << endl;
    cout << "            A" << endl;
    cout << "           / \\" << endl;
    cout << "          B   C" << endl;
    cout << "         / \\   \\" << endl;
    cout << "        D   E   F" << endl;
    cout << "           /   / \\" << endl;
    cout << "          G   H   I" << endl;
    PrintSubSeparator();
    cout << endl;

    // 手动构建二叉树
    BinaryTree<char> tree('A'); // 创建根结点A
    BinTreeNode<char> *root = tree.GetRoot();

    // 第二层
    tree.InsertLeftChild(root, 'B');
    tree.InsertRightChild(root, 'C');

    BinTreeNode<char> *nodeB = root->leftChild;
    BinTreeNode<char> *nodeC = root->rightChild;

    // 第三层
    tree.InsertLeftChild(nodeB, 'D');
    tree.InsertRightChild(nodeB, 'E');
    tree.InsertRightChild(nodeC, 'F');

    BinTreeNode<char> *nodeE = nodeB->rightChild;
    BinTreeNode<char> *nodeF = nodeC->rightChild;

    // 第四层
    tree.InsertLeftChild(nodeE, 'G');
    tree.InsertLeftChild(nodeF, 'H');
    tree.InsertRightChild(nodeF, 'I');

    cout << "二叉树构建完成！" << endl;
    cout << endl;

    // 测试遍历算法
    PrintSeparator("递归遍历算法测试");
    cout << endl;

    cout << "1. 前序遍历（根-左-右）：";
    tree.PreOrder(Write<char>);
    cout << endl;
    cout << "   预期结果：A B D E G C F H I" << endl;
    cout << endl;

    cout << "2. 中序遍历（左-根-右）：";
    tree.InOrder(Write<char>);
    cout << endl;
    cout << "   预期结果：D B G E A C H F I" << endl;
    cout << endl;

    cout << "3. 后序遍历（左-右-根）：";
    tree.PostOrder(Write<char>);
    cout << endl;
    cout << "   预期结果：D G E B H I F C A" << endl;
    cout << endl;

    // 测试二叉树的性质
    PrintSeparator("二叉树性质分析（递归算法应用）");
    cout << endl;

    cout << "1. 树的深度（高度）：" << tree.GetHeight() << endl;
    cout << "   【递归思想】树的高度 = max(左子树高度, 右子树高度) + 1" << endl;
    cout << endl;

    cout << "2. 结点总数：" << tree.GetNodeCount() << endl;
    cout << "   【递归思想】结点数 = 左子树结点数 + 右子树结点数 + 1" << endl;
    cout << endl;

    cout << "3. 叶子结点个数：" << CountLeafNodes(tree.GetRoot()) << endl;
    cout << "   【递归思想】统计左右孩子均为空的结点" << endl;
    cout << "   叶子结点：D, G, C, H, I" << endl;
    cout << endl;

    cout << "4. 单分支结点个数：" << CountSingleChildNodes(tree.GetRoot()) << endl;
    cout << "   【递归思想】统计只有一个孩子的结点" << endl;
    cout << "   单分支结点：C, E" << endl;
    cout << endl;

    cout << "5. 双分支结点个数：" << CountDoubleChildNodes(tree.GetRoot()) << endl;
    cout << "   【递归思想】统计有两个孩子的结点" << endl;
    cout << "   双分支结点：A, B, F" << endl;
    cout << endl;

    // 验证二叉树性质定理
    PrintSubSeparator();
    int n0 = CountLeafNodes(tree.GetRoot());
    int n2 = CountDoubleChildNodes(tree.GetRoot());
    cout << "【验证】二叉树性质定理：n0 = n2 + 1" << endl;
    cout << "  叶子结点数 n0 = " << n0 << endl;
    cout << "  度为2的结点数 n2 = " << n2 << endl;
    cout << "  n2 + 1 = " << n2 + 1 << endl;
    cout << "  验证结果：" << (n0 == n2 + 1 ? "正确 ✓" : "错误 ✗") << endl;
    PrintSubSeparator();
    cout << endl;

    // 测试拷贝构造
    PrintSeparator("测试拷贝构造和赋值运算");
    cout << endl;

    BinaryTree<char> tree2(tree);
    cout << "1. 拷贝构造创建tree2，中序遍历：";
    tree2.InOrder(Write<char>);
    cout << endl;
    cout << "   树的深度：" << tree2.GetHeight() << endl;
    cout << endl;

    BinaryTree<char> tree3;
    tree3 = tree;
    cout << "2. 赋值运算创建tree3，中序遍历：";
    tree3.InOrder(Write<char>);
    cout << endl;
    cout << "   树的深度：" << tree3.GetHeight() << endl;
    cout << endl;

    // 创建另一个简单的二叉树测试
    PrintSeparator("测试其他二叉树");
    cout << endl;

    cout << "构建完全二叉树：" << endl;
    cout << "            1" << endl;
    cout << "           / \\" << endl;
    cout << "          2   3" << endl;
    cout << "         / \\" << endl;
    cout << "        4   5" << endl;
    cout << endl;

    BinaryTree<int> numTree(1);
    BinTreeNode<int> *numRoot = numTree.GetRoot();

    numTree.InsertLeftChild(numRoot, 2);
    numTree.InsertRightChild(numRoot, 3);

    BinTreeNode<int> *node2 = numRoot->leftChild;
    numTree.InsertLeftChild(node2, 4);
    numTree.InsertRightChild(node2, 5);

    cout << "前序遍历：";
    numTree.PreOrder(Write<int>);
    cout << endl;

    cout << "中序遍历：";
    numTree.InOrder(Write<int>);
    cout << endl;

    cout << "后序遍历：";
    numTree.PostOrder(Write<int>);
    cout << endl;

    cout << "树的深度：" << numTree.GetHeight() << endl;
    cout << "结点总数：" << numTree.GetNodeCount() << endl;
    cout << "叶子结点数：" << CountLeafNodes(numTree.GetRoot()) << endl;
    cout << endl;

    PrintSeparator("测试完成");

    return 0;
}
