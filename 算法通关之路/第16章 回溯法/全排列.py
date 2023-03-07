# 全排列
from typing import List
class Solution:
    def permute(self,nums:List[int])->List[List[int]]:
        ans = []
        n = len(List)
        visited = set()

        def dfs(path:List[int]):
            # 退出条件： 全满
            if len(path) == n:
                ans.append(path.copy())
                return

            # 用for循环结合删除影响的方法 创造从0 1 2 3作为首的情况
            for i in range(n):
                if i not in visited:
                    path.append(nums[i])
                    visited.add(i)
                    dfs(path)
                    #消除影响
                    visited.remove(i)
                    path.pop()
                    # 第二轮循环的时候 就会出现第一项未加入循环 加入了第二项的情况

        dfs([])
        return ans