# 给定一个非空二叉树，返回其路径和（路径为一个节点到另一个节点的通路 不一定需要包括根节点）
# 自底向上的后序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def maxPathSum(self,root:TreeNode) -> int:
        self.maxSum = float('-inf')
        def helper(root:TreeNode):
            if not root:
                return 0
            maxLeft = max(helper(root.left),0)
            maxRight = max(helper(root.right),0)
            # 作为全局需要的答案
            self.maxSum = max(self.maxSum,maxLeft+maxRight+root.val)
            #返回该节点可能的最大值
            return root.val+max(maxLeft,maxRight)

        helper(root)
        return self.maxSum