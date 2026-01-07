#include "树&二叉树.h"
#include "树转二叉树.hpp"

/*
左指针还原为“第一个孩子”，
右指针还原为“下一个兄弟”。
*/
vector<TreeNode *> BinaryToForest(BinaryNode *root)
{
    vector<TreeNode *> forest;
    BinaryNode *cur = root;

    while (cur)
    {
        forest.push_back(convert(cur));
        cur = cur->right; // 下一个根（兄弟）
    }

    return forest;
}