# 冷冻期一天
from typing import List
class Solution:
    # 也可以进行空间优化 因为sell只需要i i-1 i-2，buy只需要i-1
    def maxProfit(self,prices:List[int])->int:
        if len(prices) <= 1:
            return 0
        buy, sell = [0]*len(prices),[0]*len(prices)
        buy[0] = -prices[0]
        buy[1] = max((0-prices[1]),buy[0])
        sell[1] = max((buy[0]+prices[1]),sell[0])
        for i in range(len(prices)): 
            buy[i] = max(buy[i-1],(sell[i-2]-prices[i]))
            sell[i] = max(sell[i-1],buy[i-1]+prices[i])
        return sell[-1]


