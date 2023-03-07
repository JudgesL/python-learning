# 猜数游戏
# 猜数字 告诉大/小 猜错了给猜数字的钱 猜对了获胜 计算至少需要多少钱可以保证获胜（代价最小）

# 首先二分查找查找次数最少 代价不是最少
# 最小化极大问题 需要考虑最恶劣的情况 并且把开支最小化
import sys
from typing import List
class Solution:
    def getMoneyAmount(self,n:int)->int:
        def cost(self, low:int, high:int)->int:
            if low > high:
                return 0
            res = sys.maxsize
            for i in range(low,high+1):
                tmp = i + max(cost(low,i-1),cost(i+1,high))
                res = min(res,tmp)
            return res
        return cost(1,n)
    # 记忆化递归 在取极大值时 我们需要判断i划分的两部分区域哪边继续寻找花销更大 如果我们从正中间分开
    # 显然右边更大
    def getMoneyAmount(self,n:int)->int:
        def cost(self,low:int,high:int,mem:List[List[int]])->int:
            if low > high:
                return 0
            if mem[low][high] != 0:
                return mem[low][high]
            res = sys.maxsize
            for i in range((low+high)//2,high+1):
                tmp = i + max(
                    cost(low,i-1,mem),
                    cost(i+1,high,mem),
                )
                # 尝试策略的最小
                res = min(res,tmp)
            mem[low][high] = res
            return res

        if n== 1:
            return 0
        mem = [[0]*(n+1) for _ in range(n+1)]

        return cost(1,n,mem)




