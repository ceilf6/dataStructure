#include "树&二叉树.h"

/*
左指针还原为“第一个孩子”，
右指针还原为“下一个兄弟”。
*/
TreeNode *BinaryToTree(BinaryNode *b)
{
    if (b == nullptr)
        return nullptr;

    TreeNode *t = new TreeNode;
    t->data = b->data;

    // 处理孩子链
    BinaryNode *child = b->left;
    while (child)
    {
        t->children.push_back(BinaryToTree(child));
        child = child->right; // 兄弟
    }

    return t;
}