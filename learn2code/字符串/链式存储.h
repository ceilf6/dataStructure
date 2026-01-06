struct list // 节点
{
    struct list *next; /* 指向下一个结点的指针 */
    char data;         /* 字符*/
} *point;              /* point为结构类型的指针, 指向第一结点 */

struct list
{
    struct list *next;
    char data[4]; /* 在一个结点中可放4个字符 */
} *point;
