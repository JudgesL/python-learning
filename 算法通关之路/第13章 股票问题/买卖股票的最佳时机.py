# 给定一个数组 它的第i个元素是一支给定股票的第i天的价格
# 最多允许完成一笔交易
class Solution:
    # 暴力法
    def maxProfit(self,prices):
        max_diff = 0
        for i in range(1,len(prices)):
            for j in range(0,i):
                if prices[i] - prices[j] > max_diff:
                    max_diff = prices[i] - prices[j]
        return max_diff
    # 暴力法优化
    def maxProfit_optimize(self,prices):
        max_diff = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            max_diff = max(max_diff,prices[i]-min_price)
        return max_diff