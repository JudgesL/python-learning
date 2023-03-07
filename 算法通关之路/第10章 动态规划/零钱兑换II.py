# 给定不同面额的硬币coins和一个总金额amount，编写一个函数来计算可以凑成总金额的组合数
# 如果无法凑成 返回-1
from typing import List
class Solution:
    def coinChange(self,coins:List[int],amount:int)->int:
        if amount == 0:
            return 0
        #初始化为amount+1时期大于任何可能出现的值
        dp = [0]*(amount+1)
        dp[0] = 1
        # 每多出一种硬币 对应的可能性都随之增加
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]