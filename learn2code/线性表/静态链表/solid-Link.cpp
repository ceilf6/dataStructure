#include "solid-Link.h"

SolidLink::SolidLink(int size) : maxSize(size)
{
    list = new Node[maxSize];

    // 初始化备用链表
    for (int i = 1; i < maxSize - 1; i++)
    {
        list[i].next = i + 1;
    }
    list[maxSize - 1].next = 0;

    list[0].next = 0; // 逻辑链表为空
}

SolidLink::~SolidLink()
{
    delete[] list;
}

// 分配结点
int SolidLink::malloc_node()
{
    int i = list[1].next; // 取第一个空闲结点
    if (i != 0)
        list[1].next = list[i].next;
    return i;
}

// 释放节点
void SolidLink::free_node(int i)
{
    list[i].next = list[1].next;
    list[1].next = i;
}
// 插入节点
void SolidLink::insert(int x, int k)
{
    int newNode = malloc_node();
    list[newNode].data = x;

    list[newNode].next = list[k].next;
    list[k].next = newNode;
}