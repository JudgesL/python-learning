# 假设你是专业的小偷 计划偷窃沿街的房屋 每间房内都藏有一定的现金 影响的制约因素是相邻房屋装有相互联通的防盗系统
# 如果两件相邻的房屋在同一晚上被小偷闯入 系统会自动报警 给定一个代表每个房屋存放金额的非负整数数组 不触动报警的情况下 计算最高金额
from typing import List
class Solution:
    # 递归法
    def rob(self,nums:List[int])->int:
        if len(nums) <= 0:
            return 0
        return max(self.rob(nums[1:]),nums[0]+self.rob(nums[2:]))

    # 记忆化递归
    # 显然刚才的递归里面 会反复计算例如f(3)的情况，因此增加了复杂度
    def rob_rem(self,nums:List[int])->int:
        memo = [-1 for x in range(len(nums)+1)]
        memo[-1] = 0
        return self.helper(0,nums,memo)

    def helper(self,n:int,nums:List[int],memo:List[int])->int:
        if n >= len(nums):
            return 0
        if memo[n] != -1:
            return memo[n]
        memo[n] = max(self.helper(n+1,nums,memo),self.helper(n+2,nums,memo)+nums[n])
        return memo[n]

    # 状态转移方程 helper(n) = max(helper[n+1],nums[n]+helper[n+2]) 最后答案是helper[0]
    # 动态规划
    def rob_dynamic(self,nums:List[int])->int:
        if not nums:
            return 0
        memo = [0 for x in range(len(nums)+1)]
        # 避免计算memo[-2]时memo数组溢出 避免len(nums)=0 导致出现计算-2
        memo[-2] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            memo[i] = max(memo[i+1],memo[i+2]+nums[i])
        return memo[0]

    # 空间优化的动态规划
    # 从状态转移方程看出其实只需要i+1和i+2两个量
    def rob_dynamic_optimize(self,nums:List[int])->int:
        prev = 0
        curr = 0
        for i in range(len(nums)-1,-1,-1):
            # n+2 需要变成 n+1(curr) ,n+1需要变成n（通过求值）
            temp = curr
            curr = max(curr,nums[i]+prev)
            prev = temp
        return curr