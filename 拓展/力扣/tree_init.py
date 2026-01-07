class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    #如果是多叉树的话就不能简单地用left和right，而是要用孩子列表
        self.right = right

from collections import deque

class BinaryTree:
    def __init__(self, values):
        if not values:
            self.root = None
            return

        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # 添加左子节点
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # 添加右子节点
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

tree = BinaryTree([1, 2, 3, None, 4])
