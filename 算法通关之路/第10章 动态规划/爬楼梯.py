# 正在爬楼梯 需要爬n阶才能到达楼顶，每次可以爬1或2次 有多少种不同的方法？
# 爬上第n阶台阶 就可以是从n-1走1级 或者从n-2走两级。 所以和为n-1 n-2的方法总数
class Solution:
    def climbStairs(self,n:int)->int:
        if n<2:
            return n
        dp = [0]*(n+1)
        dp[1],dp[2] = 1,2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

    def climbStairs_optimize(self,n:int)->int:
        if n < 2:
            return n
        first,second = 1,2
        for i in range(3,n+1):
            # 要把first变成second second变成first+second
            second = first + second
            first = second - first
        return second
