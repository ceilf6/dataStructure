#include "Huffman.h"

// 选出两个还没有合入、权值最小的节点的下标
template <class CharType, class WeightType>
void HuffmanTree<CharType, WeightType>::
    Select(int n, int &r1, int &r2)
{
    r1 = r2 = -1;
    for (int i = 0; i < n; i++)
        if (nodes[i].parent == -1) // 还没有合过
            if (r1 == -1)
                r1 = i;
            else if (nodes[i].weight < nodes[r1].weight)
            // 比第一小还小：第一小变第二小、第二小变第一小
            {
                r2 = r1;
                r1 = i;
            }
            else if (r2 == -1 || nodes[i].weight < nodes[r2].weight)
                // 比第二小还小
                r2 = i;
}

// 构造哈夫曼树：
// 每次从当前所有节点中选取权值最小的两个，合并成一个新节点，再放回去直到只剩一个节点
// 贪心的思想
// （用最小堆更直观）
template <class CharType, class WeightType>
void HuffmanTree<CharType, WeightType>::CreatHuffmanTree(CharType ch[], WeightType w[], int n)
{
    num = n;           // 叶子节点数
    int m = 2 * n - 1; // 总节点数
    nodes = new HuffmanTreeNode<WeightType>[m];
    LeafChars = new CharType[n];
    LeafCharCodes = new String[n];
    int i, p, q;
    // 初始化叶子节点 - 候选集
    for (i = 0; i < n; i++)
    {
        nodes[i].weight = w[i];
        nodes[i].leftChild = -1;
        nodes[i].rightChild = -1;
        nodes[i].parent = -1;
        LeafChars[i] = ch[i];
    }
    // 调用 Select 贪心构造
    for (i = n; i < m; i++)
    {
        int r1, r2;
        Select(i, r1, r2);
        nodes[r1].parent = nodes[r2].parent = i;
        nodes[i].leftChild = r1;
        nodes[i].rightChild = r2;
        nodes[i].parent = -1;
        nodes[i].weight = nodes[r1].weight + nodes[r2].weight;
    }
    // 生成哈夫曼编码 - 左0右1
    for (i = 0; i < n; i++)
    {
        LinkList<char> charCode;
        q = i;
        p = nodes[q].parent;
        while (p != -1)
        {
            if (nodes[p].leftChild == q)
                charCode.InsertElem(1, '0');
            else
                charCode.InsertElem(1, '1');
            q = p;
            p = nodes[q].parent;
        }
        LeafCharCodes[i] = charCode;
    }
}

// 遍历找叶子节点编码
template <class CharType, class WeightType>
String HuffmanTree<CharType, WeightType>::
    Encode(CharType ch)
{
    for (int i = 0; i < num; i++)
        if (LeafChars[i] == ch)
            return LeafCharCodes[i];
    throw Error("非法字符, 无法编码!");
}

// 左0右1
template <class CharType, class WeightType>
LinkList<CharType> HuffmanTree<CharType, WeightType>::Decode(String strCode)
{
    LinkList<CharType> charList;
    int p = 2 * num - 2;
    for (int i = 0; i < strCode.Length(); i++)
    {
        if (strCode[i] == '0')
            p = nodes[p].leftChild;
        else
            p = nodes[p].rightChild;
        if (nodes[p].leftChild == -1 && nodes[p].rightChild == -1)
        {
            charList.InsertElem(charList.GetLength() + 1, LeafChars[p]);
            p = 2 * num - 2;
        }
    }
    if (p != 2 * num - 2)
        throw Error("编码不对, 无法译码!");
    return charList;
}
