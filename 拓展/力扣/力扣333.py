# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
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
#题面中上面是标注的，所以不用我们自己初始化
         

class Solution:
    def largestBSTSubtree(self, root):
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root.left and not root.right:
                ans = max(ans, 1)
                return (root.val, root.val, 1)

            sz = 1
            valid = True
            l, r = root.val, root.val
            if root.left:
                L = dfs(root.left)
                if L[2] != -1 and root.val > L[1]:
                    sz += L[2]
                    l = L[0]
                else:
                    valid = False

            if root.right:
                R = dfs(root.right)
                if R[2] != -1 and root.val < R[0]:
                    sz += R[2]
                    r = R[1]
                else:
                    valid = False

            if valid:
                ans = max(ans, sz)
                return (l, r, sz)

            return (-1, -1, -1)
        
        if not root:
            return 0
        dfs(root)

        return ans

if __name__=='__main__':
    values = [10, 5, 15, 1, 8, None, 7]
    tree = BinaryTree(values)

    sol = Solution()
    result = sol.largestBSTSubtree(tree.root)
    print("最大二叉搜索子树的节点数:", result)
