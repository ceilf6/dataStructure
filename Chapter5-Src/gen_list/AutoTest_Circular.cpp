#include "GenList_Circular.h" // 广义表类

// 测试辅助函数：手动构建广义表
template <class ElemType>
GenListNode<ElemType> *BuildGenList()
{
    // 构建广义表: (a, (b, c, d), e, (f, (g, h)))
    GenListNode<char> *head = new GenListNode<char>(HEAD);
    head->ref = 1;

    // 创建原子结点 a
    GenListNode<char> *node_a = new GenListNode<char>(ATOM);
    node_a->atom = 'a';
    head->tLink = node_a;

    // 创建子表 (b, c, d)
    GenListNode<char> *node_sublist1 = new GenListNode<char>(LIST);
    GenListNode<char> *sub1_head = new GenListNode<char>(HEAD);
    sub1_head->ref = 1;
    node_sublist1->hLink = sub1_head;
    node_a->tLink = node_sublist1;

    // 子表1的元素
    GenListNode<char> *node_b = new GenListNode<char>(ATOM);
    node_b->atom = 'b';
    sub1_head->tLink = node_b;

    GenListNode<char> *node_c = new GenListNode<char>(ATOM);
    node_c->atom = 'c';
    node_b->tLink = node_c;

    GenListNode<char> *node_d = new GenListNode<char>(ATOM);
    node_d->atom = 'd';
    node_c->tLink = node_d;
    node_d->tLink = sub1_head; // 循环链表：指回头结点

    // 创建原子结点 e
    GenListNode<char> *node_e = new GenListNode<char>(ATOM);
    node_e->atom = 'e';
    node_sublist1->tLink = node_e;

    // 创建子表 (f, (g, h))
    GenListNode<char> *node_sublist2 = new GenListNode<char>(LIST);
    GenListNode<char> *sub2_head = new GenListNode<char>(HEAD);
    sub2_head->ref = 1;
    node_sublist2->hLink = sub2_head;
    node_e->tLink = node_sublist2;

    // 子表2的元素 f
    GenListNode<char> *node_f = new GenListNode<char>(ATOM);
    node_f->atom = 'f';
    sub2_head->tLink = node_f;

    // 子表2的子表 (g, h)
    GenListNode<char> *node_sublist3 = new GenListNode<char>(LIST);
    GenListNode<char> *sub3_head = new GenListNode<char>(HEAD);
    sub3_head->ref = 1;
    node_sublist3->hLink = sub3_head;
    node_f->tLink = node_sublist3;

    // 子表3的元素
    GenListNode<char> *node_g = new GenListNode<char>(ATOM);
    node_g->atom = 'g';
    sub3_head->tLink = node_g;

    GenListNode<char> *node_h = new GenListNode<char>(ATOM);
    node_h->atom = 'h';
    node_g->tLink = node_h;
    node_h->tLink = sub3_head; // 循环链表：指回头结点

    node_sublist3->tLink = sub2_head; // 循环链表：指回头结点
    node_sublist2->tLink = head;      // 循环链表：指回头结点

    return head;
}

// 简单测试函数
void SimpleTest()
{
    cout << "\n====== 简单广义表测试 ======" << endl;
    GenList<char> g1;

    // 插入几个原子元素
    g1.Insert('c');
    g1.Insert('b');
    g1.Insert('a');

    cout << "广义表 g1 = ";
    g1.Show();
    cout << endl;

    cout << "长度: " << g1.GetLength() << endl;
    cout << "深度: " << g1.GetDepth() << endl;
    cout << "原子数目: " << g1.CountAtoms() << endl;
}

// 复杂测试函数
void ComplexTest()
{
    cout << "\n====== 复杂广义表测试 ======" << endl;

    // 手动构建广义表 (a, (b, c, d), e, (f, (g, h)))
    GenListNode<char> *head = BuildGenList<char>();
    GenList<char> g2(head);

    cout << "广义表 g2 = ";
    g2.Show();
    cout << endl;

    cout << "长度: " << g2.GetLength() << endl;
    cout << "深度: " << g2.GetDepth() << endl;
    cout << "原子数目: " << g2.CountAtoms() << endl;
    cout << "\n预期原子数: 8 (a, b, c, d, e, f, g, h)" << endl;
}

// 嵌套子表测试
void NestedTest()
{
    cout << "\n====== 嵌套子表测试 ======" << endl;

    // 创建子表1: (x, y)
    GenList<char> sub1;
    sub1.Insert('y');
    sub1.Insert('x');

    cout << "子表1 = ";
    sub1.Show();
    cout << " 原子数: " << sub1.CountAtoms() << endl;

    // 创建主表，包含原子和子表
    GenList<char> main;
    main.Insert('z');
    main.Insert(sub1);
    main.Insert('w');

    cout << "主表 = ";
    main.Show();
    cout << endl;

    cout << "长度: " << main.GetLength() << endl;
    cout << "深度: " << main.GetDepth() << endl;
    cout << "原子数目: " << main.CountAtoms() << endl;
    cout << "预期原子数: 4 (w, x, y, z)" << endl;
}

// 空表测试
void EmptyTest()
{
    cout << "\n====== 空表测试 ======" << endl;
    GenList<char> empty;

    cout << "空表 = ";
    empty.Show();
    cout << endl;

    cout << "是否为空: " << (empty.IsEmpty() ? "是" : "否") << endl;
    cout << "长度: " << empty.GetLength() << endl;
    cout << "深度: " << empty.GetDepth() << endl;
    cout << "原子数目: " << empty.CountAtoms() << endl;
}

// 循环链表特性测试
void CircularTest()
{
    cout << "\n====== 循环链表特性测试 ======" << endl;
    GenList<char> g;

    g.Insert('c');
    g.Insert('b');
    g.Insert('a');

    cout << "广义表 g = ";
    g.Show();
    cout << endl;

    cout << "遍历测试(使用First和Next):" << endl;
    int count = 0;
    for (GenListNode<char> *p = g.First(); p != NULL; p = g.Next(p))
    {
        count++;
        if (p->tag == ATOM)
        {
            cout << "  元素" << count << ": 原子 '" << p->atom << "'" << endl;
        }
        else
        {
            cout << "  元素" << count << ": 子表" << endl;
        }
    }
    cout << "总共遍历了 " << count << " 个元素" << endl;
}

int main(void)
{
    cout << "\n========================================" << endl;
    cout << "  广义表循环链表实现 - 自动化测试程序" << endl;
    cout << "========================================" << endl;

    // 运行各项测试
    EmptyTest();
    SimpleTest();
    NestedTest();
    ComplexTest();
    CircularTest();

    cout << "\n====== 所有测试完成！ ======\n"
         << endl;

    return 0;
}
