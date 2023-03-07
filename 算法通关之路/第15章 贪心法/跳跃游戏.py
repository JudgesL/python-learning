# 给定一个非负整数数组 你最初位于数组的第1个位置 数组每个元素代表在该位置可以跳跃的最大长度 判断能否到达最后一个
from typing import List
class Solution:
    def canJump(self,nums:List[int])->bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1,len(nums)):
            for j in range(0,i):
                # 如果在第j个位置的最大跳跃距离大于i了 那么i可以借助j达到
                if j + nums[j] >= i:
                    dp[i] = dp[i] | dp[j]
        return dp[len(nums)-1]
    # 改变一种表示方法 让dp表示能够到的最远位置
    def canJump_optimize(self,nums:List[int])->bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            # 如果前一个位置能够达到的最远距离无法触及这个位置
            if dp[i-1] < i:
                dp[i] = dp[i-1]
            else:
                # 可以从dp[i]起跳
                dp[i] = max(dp[i-1],nums[i]+i)
        # n-1已经是最后一个了
        return dp[n-1] >= n-1
    # 贪心算法 但是贪两步 我们不看这一步最远能到哪 而是看下一步能选择的区域有多广 也就是跳了以后的落点他能够到的区域有多宽
    def canJump_greedy(self,nums:List[int])->bool:
        begin,end = 0,0
        while True:
            next_end = end
            # 避免越界
            # 从0开始起跳
            for i in range(begin,min(end+1,len(nums))):
                print('判断的格子为：',i)
                # next_end是已经能到达的范围(i=0) 之前的选择里能到达的最大范围(i>0) next_end指示最远能选择的范围
                next_end = max(next_end,i+nums[i])
            # 如果下一步能抵达的范围并不超过这一步能抵达的范围 也并不超过之前的最长范围，那么就没有希望了 可以确定无法抵达终点
            # 当begin抵达了终点 循环无法进行 也会导致这个结果 也就是该循环的退出点
            print('next_end == end:',next_end == end)
            if next_end == end:
                break
            # 这一个格子通过一跳后的视野已经确定 用他更新可跳跃的最远范围 然后我们开始考察下一个格子 直到出现了死局或者终点
            begin,end = end+1,next_end
            print('end:',end)
            # 其实早就可以判断 next_end是否> len(nums)+1来退出了
        return end>=len(nums) + 1

solve = Solution()
nums = [2,3,1,1,4]
res = solve.canJump_greedy(nums)
print(res)
