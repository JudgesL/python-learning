# 和上一题几乎完全一样
from typing import List
class Solution:
    # 记忆化递归
    def PredictTheWinner(self,nums:List[int])->bool:
        sum = 0
        for i in nums:
            sum += i
        mem = []
        for i in range(len(nums)):
            mem.append([0]*len(nums))
        return 2*self.find_max(0,len(nums)-1,nums,mem) >= sum

    def find_max(self,left:int,right:int,nums:List[int],mem:List[List[int]])->int:
        if left<0 or right<0 or left>right:
            return 0
        if mem[left][right] != 0:
            return mem[left][right]
        if left == right:
            mem[left][right] = nums[left]
            return nums[left]
        max_num = max(nums[left]+ min(
                                        self.find_max(left+2,right,nums,mem),
                                        self.find_max(left+1,right-1,nums,mem),),
                      nums[right]+ min(
                                        self.find_max(left+1,right-1,nums,mem),
                                        self.find_max(left,right-2,nums,mem),))
        mem[left][right] = max_num
        return max_num

        # 动态规划
        # 详细可以参考书本
    def PredictTheWinner2(self,nums:List[int])->bool:
        n = len(nums)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        # 计算上三角
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = max(nums[i] - dp[i+1][j],
                               nums[j] - dp[i][j-1])
        return dp[0][n-1] >= 0

    