# 给定无重复元素数组candidates和目标数target 判断所有和为target的组合 candidate可以无限次选取
from typing import List
class Solution:
    def combinationSum(self,candidates:List[int],target:int)->List[List[int]]:
        ans = []
        n = len(candidates)

        def dfs(idx:int,cur:int,path:List[int]):
            #结束条件 1.找到解 2.长度极限
            if cur == 0:
                ans.append(path.copy())
                return
            elif idx == n:
                return

            # 考虑可能的解
            if candidates[idx] <= cur:
                path.append(candidates[idx])
                # 继续考虑当前
                dfs(idx,cur-candidates[idx],path)
                # 消除影响
                path.pop()
            # 不加入这个数字 考虑下一个数字
            dfs(idx+1,cur,path)

        dfs(0,target,[])
        return ans

solve = Solution()
print(solve.combinationSum([2,3,5],8))

