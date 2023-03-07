from typing import List
class Solution:
    # 可以进一步优化空间 buy->prebuy sell-> presell
    def maxProfit(self,prices:List[int],fee:int)->int:
        if len(prices) <= 1:
            return 0
        buy,sell = [0]*len([prices]),[0]*len(prices)
        buy[0] = -prices[0]
        for i in range(1,len(prices)):
            # 什么事情都不干 和卖了之前的买现在的 哪个更高选哪个
            buy[i] = max(buy[i-1],sell[i-1]-prices[i])
            sell[i] = max(sell[i-1],buy[i-1]+prices[i]-fee)
        return sell[-1]