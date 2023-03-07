# 假设你是专业的小偷 计划偷窃沿街的房屋 每间房内都藏有一定的现金 影响的制约因素是相邻房屋装有相互联通的防盗系统
# 如果两件相邻的房屋在同一晚上被小偷闯入 系统会自动报警 给定一个代表每个房屋存放金额的非负整数数组 不触动报警的情况下 计算最高金额
# 增加了一个条件 首位房间是相连的

# 增加了这个条件 显然就是需要我们在偷首和尾之间做出选择 也就是在[0,n-1)和[1,n)之间求出最大值
from typing import List
class Solution:
    def rob(self,nums:List[int])->int:
        if len(nums) == 1:
            return nums[0]
        prev = 0
        curr = 0

        for i in range(len(nums)-1):
            # n+2 需要变成 n+1(curr) ,n+1需要变成n（通过求值）
            temp = curr
            curr = max(curr,nums[i]+prev)
            prev = temp
        res = curr

        prev = 0
        curr = 0
        for i in range(1,len(nums)):
            temp = curr
            curr = max(curr, nums[i] + prev)
            prev = temp
        res2 = curr

        return max(res,res2)

