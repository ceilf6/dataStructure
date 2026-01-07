#include "重载运算符-简化字符串操作.h"

template <class WeightType>
struct HuffmanTreeNode
{
    WeightType weight;
    int parent, leftChild, rightChild;

    HuffmanTreeNode();
    HuffmanTreeNode(WeightType w,
                    int p = -1, int lChild = -1, int rChild = -1);
};

template <class CharType, class WeightType>
class HuffmanTree
{
protected:
    HuffmanTreeNode<WeightType> *nodes;
    CharType *LeafChars;
    String *LeafCharCodes;
    int num;
    void Select(int n, int &r1, int &r2);
    void CreatHuffmanTree(CharType ch[], WeightType w[], int n);

public:
    HuffmanTree(CharType ch[], WeightType w[], int n);
    virtual ~HuffmanTree();
    String Encode(CharType ch);
    LinkList<CharType> Decode(String strCode);
    HuffmanTree(
        const HuffmanTree<CharType, WeightType> &t);
    HuffmanTree<CharType, WeightType> &operator=(
        const HuffmanTree<CharType, WeightType> &t);
};
