enum triple
{
    var, // HEAD
    num, // ATOM
    ptr  // LIST
};
class polynode
{                    // 多项式结点类定义
    polynode *tlink; // 同一层下一结点指针
    int exp;         // 指数
    triple tag;      // 标志,var:表头结点,ptr:指向子表头节点,num:原子结点
    union            // 联合
    {
        char vble;       // HEAD: 表头结点中存放该链表基于的变元名
        polynode *hlink; // LIST: 子表结点中存放指向系数子链表的指针
        int coef;        // ATOM: 原子结点中存放实数型系数
    };
};
