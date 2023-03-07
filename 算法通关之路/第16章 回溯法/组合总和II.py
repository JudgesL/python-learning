# 每个数字在组合只能使用一次 数组中有可能有重复的数字
from typing import List
class Solution:
    def combinationSum2(self,candidates:List[int],target:int)->List[List[int]]:
        ans = []
        n = len(candidates)
        visited = set()
        candidates.sort()

        def dfs(idx:int,cur:int,path:List[int]):
            if cur == 0:
                ans.append(path.copy())
                return
            elif idx == n:
                return

            # 如果这个数字和前一个数字是一样的 但是前一个数字不在路径中 那个这个数字也必定不必要出现在路径中
            if (idx!=0 and candidates[idx] == candidates[idx-1] and ((idx-1) not in visited)):
                dfs(idx+1,cur,path)
                # 在这边直接打断这个链接 后续不需要考虑加不加入这个数字了 已经决定了
                return
            # 加入这个数字
            if candidates[idx] <= cur and (idx not in visited):
                path.append(candidates[idx])
                visited.add(idx)
                dfs(idx+1,cur - candidates[idx],path)
                # 消除影响
                visited.remove(idx)
                path.pop()
            # 不加入
            dfs(idx+1,cur,path)
        dfs(0,target,[])
        return ans


