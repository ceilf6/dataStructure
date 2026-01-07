#include <vector>

using namespace std;

struct TreeNode
{
    char data;
    vector<TreeNode *> children;
};

struct BinaryNode
{
    char data;
    BinaryNode *left;  // 第一个孩子
    BinaryNode *right; // 下一个兄弟
};