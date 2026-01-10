#include "邻接表.h"

// 一条边结点有两个“next 指针”: 分叉的链表
struct EdgeNode
{
    int ivex, jvex;  // 边的两个端点下标
    EdgeNode *ilink; // 在 ivex 的边链表中的下一条边
    EdgeNode *jlink; // 在 jvex 的边链表中的下一条边
};