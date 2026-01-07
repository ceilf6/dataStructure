#include "树转二叉树.h"

// 递归转换兄弟链
/*
    1.	每个结点的第一个孩子 → 二叉树的左孩子
    2.	同一层中相邻的兄弟 → 二叉树的右孩子
    3.	其余孩子全部通过“右兄弟链”连接
    然后对右兄弟链做同样的处理，直到小于等于两个

    转换前
        A
      / | \
     B  C  D
        |
        E

    转换后
        A
       /
      B
       \
        C
       / \
      E   D
*/
BinaryNode *convert(TreeNode *root)
{
    if (!root)
        return nullptr;

    BinaryNode *b = new BinaryNode{root->data, nullptr, nullptr};

    if (!root->children.empty())
    {
        b->left = convert(root->children[0]);

        BinaryNode *cur = b->left;
        for (int i = 1; i < root->children.size(); i++)
        {
            cur->right = convert(root->children[i]);
            cur = cur->right;
        }
    }
    return b;
}