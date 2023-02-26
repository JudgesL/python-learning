# 给定一个二叉树和一个目标和 判断该树中是否存在根节点到叶子节点的路径 这条路径上所有节点值相加等于目标和
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS 递归
    def hasPathSum(self,root:TreeNode,sum:int) -> bool:
        if not root:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
    # DFS 迭代
    def hasPathSum_diedai(self,root:TreeNode,sum:int)->bool:
        if root is None:
            return False
        stack = [(root,sum-root.val)]
        while stack:
            node, remain = stack.pop()
            if not node.left and not node.right and remain == 0:
                return True
            if node.right:
                stack.append((node.right,remain - node.right.val))
            if node.left:
                stack.append((node.left,remain - node.left.val))
        return False
