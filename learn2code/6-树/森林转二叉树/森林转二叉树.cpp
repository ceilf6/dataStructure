#include "树&二叉树.h"
#include "树转二叉树.hpp"

/*
和树转二叉树类似
森林转二叉树 = 先把森林中的各棵树用“右兄弟”连起来，再按“左孩子–右兄弟”法转成二叉树

   A        D        G
  /        / \
 B        E   F
 |
 C


         A
       /
      B
     /
    C
     \
      D
     / \
    E   F
     \
      G
*/
BinaryNode *TreesToBinary(TreeNode *t[], int n)
{
    if (t == nullptr || n == 0)
        return nullptr;

    // 1. 第一棵树 → 二叉树根
    BinaryNode *root = convert(t[0]);

    // 2. 其余树 → 根的右兄弟
    BinaryNode *cur = root;
    for (int i = 1; i < n; i++)
    {
        cur->right = convert(t[i]);
        cur = cur->right;
    }

    return root;
}