# 给定一个二叉树和一个目标和 找到所有从根节点到叶子节点路径总和等于给定目标和的路径
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self,root:TreeNode,sum:int) -> List[List[int]]:
        def helper(root:TreeNode, sum:int, path:List):
            if not root:
                return
            if not root.left and not root.right and sum - root.val == 0:
                path += [root.val]
                ans.append(path)
            helper(root.left, sum-root.val,path+[root.val])
            helper(root.right,sum-root.val,path+[root.val])

        ans = []
        helper(root,sum,[])
        return ans

    def pathSum_diedai(self, root:TreeNode,sum:int)->List[List[int]]:
        if not root:
            return []
        stack =[(root,[root.val],root.val)]
        ans = []
        while stack:
            node,path,total = stack.pop()
            if not node.right and not node.left and total == sum:
                ans.append(path)
            if node.right:
                stack.append((node.right,path+[node.right.val],total+node.right.val))
            if node.left:
                stack.append((node.left,path+[node.left.val],total+node.left.val))
        return ans

