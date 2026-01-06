/*
  - 单向递归的特点是依赖链是线性的，可以用简单变量迭代
  - 二分合并是树状分治，不算单向递归
  - 但它也能用循环消除，方法是自底向上逐层合并，模拟树的层序遍历（从叶子到根）
*/

var mergeKLists = function (lists) {
    // 边界处理体现细节
    if (lists.length === 0) return null;

    function merge2List(pt1, pt2) {
        if (pt1 === null) return pt2;
        else if (pt2 === null) return pt1;
        else if (pt1.val < pt2.val) {
            pt1.next = merge2List(pt1.next, pt2);
            return pt1;
        } else {
            pt2.next = merge2List(pt1, pt2.next);
            return pt2;
        }
    }

    // 以下标作为分治基础
    function merge(lists, left, right) {
        if (left >= right) return lists[left];
        const mid = Math.floor((left + right) / 2)
        const l1 = merge(lists, left, mid);
        const l2 = merge(lists, mid + 1, right);
        return merge2List(l1, l2);
    }

    return merge(lists, 0, lists.length - 1)
}

/*
  循环版本：自底向上，每轮两两合并

  原理：模拟分治树的层序遍历（从叶子到根）

  第0轮: [L0] [L1] [L2] [L3] [L4] [L5]   (6个链表)
  第1轮: [L0+L1] [L2+L3] [L4+L5]         (3个链表)
  第2轮: [L01+L23] [L45]                 (2个链表)
  第3轮: [L0123+L45]                     (1个链表，完成)
*/
var mergeKListsLoop = function (lists) {
    if (lists.length === 0) return null;

    // 合并两个链表（循环版本，避免递归）
    function merge2List(pt1, pt2) {
        const dummy = { next: null };
        let cur = dummy;
        while (pt1 !== null && pt2 !== null) {
            if (pt1.val < pt2.val) {
                cur.next = pt1;
                pt1 = pt1.next;
            } else {
                cur.next = pt2;
                pt2 = pt2.next;
            }
            cur = cur.next;
        }
        cur.next = pt1 !== null ? pt1 : pt2;
        return dummy.next;
    }

    // 自底向上：每轮两两合并，直到只剩1个
    let n = lists.length;
    while (n > 1) {
        const k = Math.floor((n + 1) / 2); // 合并后的链表数
        for (let i = 0; i < Math.floor(n / 2); i++) {
            lists[i] = merge2List(lists[2 * i], lists[2 * i + 1]);
        }
        if (n % 2 === 1) {
            // 奇数个，最后一个直接保留
            lists[k - 1] = lists[n - 1];
        }
        n = k;
    }

    return lists[0];
}