from typing import List
# 分析以后发现 因为限制了交易次数
# 所以我们在求sell[i][j]的时候会遇到什么？sell[i][j] = max(buy[i][j-1]+prices[j],sell[i][j-1])吗？
# 不是！ 因为如果限制了1次交易 那这个max其实指的是buy[i][?]到buy[i][j-1]之间的最大值，或者说是成本的最小值。 其他值是没有意义的
# 那么 如何衡量成本最小值 成本即支出 首先我们应当初始化为price[0] 然后如果买入会导致亏本，那就不应该买
# 如果我们维护的min_price更小，支出（price[j])-盈利（dp[i-1][j-1])更大，那就是亏本买卖。
# 为什么每轮会初始化min_price为price[0] 因为如果不能低于price[0]一切操作都毫无意义

class Solution:
    def maxProfit(self,prices:List[int],k:int)->int:
        if len(prices) <= 1:
            return 0
        dp = [[0]*len(prices)]*(k+1)
        print(dp)
        for i in range(1,k+1):
            min_price = prices[0]
            for j in range(1,len(prices)):
                min_price = min(min_price,prices[j]-dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1],prices[j]-min_price)
        return dp[k][len(prices)-1]

    # 上面的做法略微有些不自然 如果我们用交易日作为主循环变量的话
    def maxProfit_op(self,prices:List[int],k:int)->int:
        if len(prices) <= 1:
            return 0
        dp = [0]*(k+1)
        min_price = [prices[0]]*(k+1)
        for i in range(1,len(prices)):
            for j in range(1,k+1):
                print('现在的天数：',i)
                print('交易次数：',j)
                # 最低成本是 什么都不干（i=1,j=1初始值）或上次交易时候的最低成本（例如i=2,j=2) 和 现在价格-上次交易中盈利最大值
                # 毕竟我们的时间是主变量 所以这个min_price是在衡量 在同一交易次数的情况下，到底在哪一天卖更好。
                # 比如同是1次交易。 在第1天成本-2（买入） 在第4天成本是0（更优的买入）
                # 如果同是2次交易。 第2天成本是2（2买2卖2买）第3天成本是1（2买6卖5买） 第4天成本就是用第3天成本1 和第3天没买第4天买(0-（6-2）)对比，是-4
                # 这就意味着 第2次交易在第4天会比第3天更好。 所以price其实是在不断衡量同交易次数下 哪天交易更好。dp则记录了选择当下的最好方法做交易能获得的最大值
                # 也就是说在i=3时，dp[j]记录了在第3天的情况下，做j次交易能获得的最大收益
                min_price[j] = min(min_price[j],prices[i]-dp[j-1])
                print('最小成本:',min_price[j])
                # 如果在这个时间点交易 收入是这次的卖出额-成本
                dp[j] = max(dp[j],prices[i]-min_price[j])
        return dp[k]
solve = Solution()
prices = [3,2,6,5,0,3]
k = 2
print(solve.maxProfit_op(prices,k))