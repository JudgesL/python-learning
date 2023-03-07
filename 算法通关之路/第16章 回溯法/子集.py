from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(idx,path:List[int]):
            # 终止条件
            if idx == n:
                ans.append(path.copy())
                return
            # 加入
            path.append(nums[idx])
            dfs(idx+1,path)
            # 消除影响
            path.pop()
            # 不加入
            dfs(idx+1,path)

        dfs(0,[])
        return ans
