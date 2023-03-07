# 给定不同面额的硬币coins和一个总金额amount，编写一个函数来计算可以凑成总金额所需的最少的硬币个数
# 如果无法凑成 返回-1
from typing import List
class Solution:
    def coinChange(self,coins:List[int],amount:int)->int:
        if amount == 0:
            return 0
        #初始化为amount+1时期大于任何可能出现的值
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        # 这里使用的是递推而不是递归
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return -1 if dp[amount] == (amount+1) else dp[amount]